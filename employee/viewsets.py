from .models import Employee
from .serializers import EmployeeSerializer,EmployeeCreateSerializer,EmployeeDetailsSerializer,EmployeePatchSerializer
from rest_framework import viewsets, status
from rest_framework.views import APIView
from rest_framework_simplejwt.authentication import JWTAuthentication
from rest_framework.permissions import IsAuthenticated, AllowAny
from rest_framework.response import Response
from django.views.decorators.cache import cache_page


class EmployeeViewSet(viewsets.ViewSet):
    # serializer_class = EmployeeSerializer
    # queryset = Employee.objects.all()

    # def get_serializer(self, *args, **kwargs):
    #     serializer_mapping = {
    #         'POST': EmployeeSerializer,
    #         'PATCH': EmployeeSerializer,
    #         'GET': EmployeeSerializer,
    #     }
    #     method = self.request.method
    #     return serializer_mapping.get(method, EmployeeSerializer)(*args, **kwargs)
    permission_classes = [IsAuthenticated]
    authentication_classes = [JWTAuthentication]

    # @method_decorator(cache_page(60))
    def list(self,request):
      queryset = Employee.objects.all()
      serializer = EmployeeSerializer(queryset, many = True)