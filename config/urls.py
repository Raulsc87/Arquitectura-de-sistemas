from django.contrib import admin
from django.urls import include, path
from rest_framework.routers import DefaultRouter
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
    TokenVerifyView,
)

from clientes.views import ClienteViewSet, ContactoViewSet, DireccionViewSet
from productos.views import CategoriaViewSet, InventarioViewSet, ProductoViewSet
from proveedores.views import CompraViewSet, DetalleCompraViewSet, ProveedorViewSet
from usuarios.views import PermisoViewSet, RolViewSet, UsuarioViewSet
from ventas.views import DetalleVentaViewSet, PagoViewSet, VentaViewSet


router = DefaultRouter()

router.register("permisos", PermisoViewSet)
router.register("roles", RolViewSet)
router.register("usuarios", UsuarioViewSet)

router.register("clientes", ClienteViewSet)
router.register("direcciones", DireccionViewSet)
router.register("contactos", ContactoViewSet)

router.register("categorias", CategoriaViewSet)
router.register("productos", ProductoViewSet)
router.register("inventarios", InventarioViewSet)

router.register("ventas", VentaViewSet)
router.register("detalles-venta", DetalleVentaViewSet)
router.register("pagos", PagoViewSet)

router.register("proveedores", ProveedorViewSet)
router.register("compras", CompraViewSet)
router.register("detalles-compra", DetalleCompraViewSet)


urlpatterns = [
    path("admin/", admin.site.urls),
    path("api/token/", TokenObtainPairView.as_view(), name="token_obtain_pair"),
    path("api/token/refresh/", TokenRefreshView.as_view(), name="token_refresh"),
    path("api/token/verify/", TokenVerifyView.as_view(), name="token_verify"),
    path("api/", include(router.urls)),
]
