from django.urls import path, include
from rest_framework.routers import DefaultRouter

from .views import UrlController

urlpatterns = [
    # Other URL patterns for your app...
    path('create_url/', UrlController.as_view({'post': 'post'})),
    path('<id>', UrlController.as_view({'get': 'redirect'})),
]