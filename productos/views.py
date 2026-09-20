from config.api import SoftDeleteModelViewSet

from .models import Categoria, Inventario, Producto
from .serializers import (
    CategoriaSerializer,
    InventarioSerializer,
    ProductoSerializer,
)


class CategoriaViewSet(SoftDeleteModelViewSet):
    queryset = Categoria.objects.all()
    serializer_class = CategoriaSerializer


class ProductoViewSet(SoftDeleteModelViewSet):
    queryset = Producto.objects.all()
    serializer_class = ProductoSerializer


class InventarioViewSet(SoftDeleteModelViewSet):
    queryset = Inventario.objects.all()
    serializer_class = InventarioSerializer