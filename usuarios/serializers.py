from rest_framework import serializers

from .models import Permiso, Rol, Usuario


CAMPOS_SOLO_LECTURA = (
    "id",
    "is_deleted",
    "deleted_at",
    "created_at",
    "updated_at",
)


class PermisoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Permiso
        fields = "__all__"
        read_only_fields = CAMPOS_SOLO_LECTURA


class RolSerializer(serializers.ModelSerializer):
    class Meta:
        model = Rol
        fields = "__all__"
        read_only_fields = CAMPOS_SOLO_LECTURA


class UsuarioSerializer(serializers.ModelSerializer):
    class Meta:
        model = Usuario
        fields = "__all__"
        read_only_fields = CAMPOS_SOLO_LECTURA