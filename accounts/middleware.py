from django.utils import timezone

from rest_framework_simplejwt.authentication import JWTAuthentication
from django.utils.functional import SimpleLazyObject
from django.contrib.auth.middleware import get_user

from .models import User


class UpdateLastActivityMiddleware(object):
    @staticmethod
    def get_user(request):
        user = get_user(request)
        token_authentication = JWTAuthentication()
        try:
            user, _token = token_authentication.authenticate(request)
        except:
            pass
        return user

    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        request.user = SimpleLazyObject(lambda: self.__class__.get_user(request))
        response = self.get_response(request)

        if request.user.is_authenticated:
            User.objects.filter(id=request.user.id).update(last_activity=timezone.now())
        return response