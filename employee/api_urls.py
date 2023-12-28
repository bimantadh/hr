from django.urls import path, include
from rest_framework import routers
from .viewsets import EmployeeViewSet

router = routers.DefaultRouter()
router.register(r'',EmployeeViewSet, basename = 'employees')


urlpatterns= [
    path('', include(router.urls)),
]