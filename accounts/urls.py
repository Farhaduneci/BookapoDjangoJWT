from django.urls import path

from rest_framework_simplejwt.views import TokenRefreshView
from .views import CustomTokenObtainPairView

from .views import RegisterView

# Login/Logout routes are not usually placed under a common 'account'
# path. They are usually placed under a common 'api' path.
# But for the sake of simplicity, I place them here.

urlpatterns = [
    path("token/", CustomTokenObtainPairView.as_view(), name="token_obtain_pair"),
    path("token/refresh/", TokenRefreshView.as_view(), name="token_refresh"),
    path("register/", RegisterView.as_view(), name="sign_up"),
]
