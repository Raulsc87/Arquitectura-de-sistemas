from config.api import SoftDeleteModelViewSet

from .models import Permiso, Rol, Usuario
from .serializers import PermisoSerializer, RolSerializer, UsuarioSerializer


class PermisoViewSet(SoftDeleteModelViewSet):
    queryset = Permiso.objects.all()
    serializer_class = PermisoSerializer


class RolViewSet(SoftDeleteModelViewSet):
    queryset = Rol.objects.all()
    serializer_class = RolSerializer


class UsuarioViewSet(SoftDeleteModelViewSet):
    queryset = Usuario.objects.all()
    serializer_class = UsuarioSerializer