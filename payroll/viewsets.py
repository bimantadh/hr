from .models import Pay
from payroll.serializers import PaySerializer
from rest_framework import viewsets

class PayViewSet(viewsets.ModelViewSet):
    serializer_class = PaySerializer
    queryset = Pay.objects.all()

    def get_serializer(self, *args, **kwargs):
        serializer_mapping = {
            'POST': PaySerializer,
            'PATCH': PaySerializer,
            'GET': PaySerializer,
        }
        method = self.request.method
        return serializer_mapping.get(method, PaySerializer)(*args, **kwargs)