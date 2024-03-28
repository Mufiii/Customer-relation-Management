from django.urls import path
from .views import AdminRegistrationAPIView , AdminLoginAPIView

urlpatterns = [
  
    path('register/',
          AdminRegistrationAPIView.as_view(),
          name='register'
    ),
    path('login/',
          AdminLoginAPIView.as_view(),
          name='login'
    ),
]
