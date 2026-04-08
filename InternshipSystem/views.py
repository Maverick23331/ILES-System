from rest_framework_simplejwt.views import TokenObtainPairView
from rest_framework.throttling import UserRateThrottle
from .throttles import LoginThrottle

class LoginView(TokenObtainPairView):
    throttle_classes = [LoginThrottle]