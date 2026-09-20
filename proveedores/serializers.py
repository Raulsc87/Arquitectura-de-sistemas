from rest_framework import serializers

from .models import Compra, DetalleCompra, Proveedor


CAMPOS_SOLO_LECTURA = (
    "id",
    "is_deleted",
    "deleted_at",
    "created_at",
    "updated_at",
)


class ProveedorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Proveedor
        fields = "__all__"
        read_only_fields = CAMPOS_SOLO_LECTURA


class CompraSerializer(serializers.ModelSerializer):
    class Meta:
        model = Compra
        fields = "__all__"
        read_only_fields = CAMPOS_SOLO_LECTURA


class DetalleCompraSerializer(serializers.ModelSerializer):
    class Meta:
        model = DetalleCompra
        fields = "__all__"
        read_only_fields = CAMPOS_SOLO_LECTURA