from payroll.models import Pay
from rest_framework import serializers

class PaySerializer(serializers.ModelSerializer):

    class Meta:
        model = Pay
        fields = ['id', 'payroll_name','deposited_date', 'amount']