from django.urls import path
from api.views.auth_view import UserRegistrationAPIView, UserLoginAPIView


urlpatterns = [
    path('register/', UserRegistrationAPIView.as_view(), name='register'),
    path('login/', UserLoginAPIView.as_view(), name='login'),
]
