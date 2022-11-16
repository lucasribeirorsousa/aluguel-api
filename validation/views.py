from rest_framework import viewsets

from .models import Validation
from .serializers import ValidationSerializer


class ValidationViewSet(viewsets.ModelViewSet):
    queryset = Validation.objects.all()
    serializer_class = ValidationSerializer
