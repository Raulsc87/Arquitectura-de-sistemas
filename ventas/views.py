from config.api import SoftDeleteModelViewSet

from .models import DetalleVenta, Pago, Venta
from .serializers import (
    DetalleVentaSerializer,
    PagoSerializer,
    VentaSerializer,
)


class VentaViewSet(SoftDeleteModelViewSet):
    queryset = Venta.objects.all()
    serializer_class = VentaSerializer


class DetalleVentaViewSet(SoftDeleteModelViewSet):
    queryset = DetalleVenta.objects.all()
    serializer_class = DetalleVentaSerializer


class PagoViewSet(SoftDeleteModelViewSet):
    queryset = Pago.objects.all()
    serializer_class = PagoSerializer