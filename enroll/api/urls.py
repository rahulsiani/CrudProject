from django.urls import path, include
from enroll.api import views
from rest_framework.routers import DefaultRouter

# Craeting Router Object
router = DefaultRouter()

# Register StudenViewSet With Router
router.register('crud', views.UserViewSet, basename='user')
# router.register('song', views.SongViewSet, basename='song')

urlpatterns = [
    path ('', include(router.urls)),
]
