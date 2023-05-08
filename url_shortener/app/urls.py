from django.urls import path, include
from rest_framework.routers import DefaultRouter

from .views import UrlController

urlpatterns = [
    # Other URL patterns for your app...
    path('<short_url>', UrlController.as_view({'get': 'redirect'})),
    path('create_url/', UrlController.as_view({'post': 'post'})),
]
