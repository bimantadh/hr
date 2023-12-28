from django.urls import path, include
from rest_framework import routers
from .viewsets import PayViewSet

router = routers.DefaultRouter()
router.register(r'',PayViewSet, basename = 'payrolls')


urlpatterns= [
    path('', include(router.urls)),
]