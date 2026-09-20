from rest_framework import serializers

from .models import Categoria, Inventario, Producto


CAMPOS_SOLO_LECTURA = (
    "id",
    "is_deleted",
    "deleted_at",
    "created_at",
    "updated_at",
)


class CategoriaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Categoria
        fields = "__all__"
        read_only_fields = CAMPOS_SOLO_LECTURA


class ProductoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Producto
        fields = "__all__"
        read_only_fields = CAMPOS_SOLO_LECTURA


class InventarioSerializer(serializers.ModelSerializer):
    class Meta:
        model = Inventario
        fields = "__all__"
        read_only_fields = CAMPOS_SOLO_LECTURA