from .models import Employee
from rest_framework import serializers, validators


# class EmployeeSerializer(serializers.ModelSerializer):

#     class Meta:
#         model = Employee
#         fields = ['id', 'first_name','last_name' ]

class EmployeeSerializer(serializers.Serializer):
    id= serializers.IntegerField()
    first_name = serializers.CharField()



class EmployeeDetailsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Employee
        exclude = ['password']


class EmployeeCreateSerializer(serializers.Serializer):
    id = serializers.ReadOnlyField()
    first_name =serializers.CharField(max_length= 10 , min_length = 3)
    last_name =serializers.CharField(required = False)
    department = serializers.CharField(required =False)
    email = serializers.EmailField(
        validators=[
        validators.UniqueValidator(queryset=Employee.objects.all())
        ]
    )
    password = serializers.CharField()
    phone = serializers.CharField(required=False)

class EmployeePatchSerializer(serializers.Serializer):
    first_name = serializers.CharField(required=False, max_length=10, min_length=3)
    last_name = serializers.CharField(required=False)
    department = serializers.CharField(required =False)
    email = serializers.EmailField(
        required=False,
        validators=[
        validators.UniqueValidator(queryset=Employee.objects.all())
        ]
    )
    password = serializers.CharField(required=False)
    phone = serializers.CharField(required=False)