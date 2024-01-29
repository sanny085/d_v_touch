# userapp/urls.py
from django.urls import path
from .views import hello_touch

urlpatterns = [
   path('users/', hello_touch, name='hello_touch'),
]
