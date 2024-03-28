from django.urls import path , include
from .views import LeedsAPIView


urlpatterns = [
    path('leeds/',LeedsAPIView.as_view(),name='leeds')
]
