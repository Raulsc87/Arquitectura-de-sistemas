from config.api import SoftDeleteModelViewSet

from .models import Cliente, Contacto, Direccion
from .serializers import (
    ClienteSerializer,
    ContactoSerializer,
    DireccionSerializer,
)


class ClienteViewSet(SoftDeleteModelViewSet):
    queryset = Cliente.objects.all()
    serializer_class = ClienteSerializer


class DireccionViewSet(SoftDeleteModelViewSet):
    queryset = Direccion.objects.all()
    serializer_class = DireccionSerializer


class ContactoViewSet(SoftDeleteModelViewSet):
    queryset = Contacto.objects.all()
    serializer_class = ContactoSerializer