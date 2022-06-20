from django.urls import path, include
from rest_framework.routers import DefaultRouter

from manual import views


router = DefaultRouter()
router.register(r'api/manuals', views.ManualVersionViewSet, basename='manuals')
router.register(r'api/elems', views.ManualElemViewSet, basename='elements')

urlpatterns = [
    path('', include(router.urls)),
]
