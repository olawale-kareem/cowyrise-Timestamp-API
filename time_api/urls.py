from django.urls import path
from .views import TimeStampListAPIView

urlpatterns = [
    path('time-stamps', TimeStampListAPIView.as_view(), name='time-stamps')
]
