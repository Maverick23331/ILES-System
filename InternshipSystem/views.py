from rest_framework_simplejwt.views import TokenObtainPairView
from rest_framework.throttling import UserRateThrottle
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from .throttles import LoginThrottle

class LoginView(TokenObtainPairView):
    throttle_classes = [LoginThrottle]

class UserView(APIView):
    """Get current authenticated user info"""
    permission_classes = [IsAuthenticated]
    
    def get(self, request):
        user = request.user
        return Response({
            'id': user.id,
            'username': user.username,
            'email': user.email,
            'first_name': user.first_name,
            'last_name': user.last_name,
        })