from config.api import SoftDeleteModelViewSet

from .models import Compra, DetalleCompra, Proveedor
from .serializers import (
    CompraSerializer,
    DetalleCompraSerializer,
    ProveedorSerializer,
)


class ProveedorViewSet(SoftDeleteModelViewSet):
    queryset = Proveedor.objects.all()
    serializer_class = ProveedorSerializer


class CompraViewSet(SoftDeleteModelViewSet):
    queryset = Compra.objects.all()
    serializer_class = CompraSerializer


class DetalleCompraViewSet(SoftDeleteModelViewSet):
    queryset = DetalleCompra.objects.all()
    serializer_class = DetalleCompraSerializer