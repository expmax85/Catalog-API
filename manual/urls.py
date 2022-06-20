from django.urls import path, include
from rest_framework import routers

from manual import views


router = routers.DefaultRouter()
router.register(r'manuals', views.ManualVersionViewSet, basename='manuals')
router.register(r'elems', views.ManualElemViewSet, basename='elements')

urlpatterns = [
    path('api/', include(router.urls)),
]
