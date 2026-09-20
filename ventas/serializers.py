from rest_framework import serializers

from .models import DetalleVenta, Pago, Venta


CAMPOS_SOLO_LECTURA = (
    "id",
    "is_deleted",
    "deleted_at",
    "created_at",
    "updated_at",
)


class VentaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Venta
        fields = "__all__"
        read_only_fields = CAMPOS_SOLO_LECTURA


class DetalleVentaSerializer(serializers.ModelSerializer):
    class Meta:
        model = DetalleVenta
        fields = "__all__"
        read_only_fields = CAMPOS_SOLO_LECTURA


class PagoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Pago
        fields = "__all__"
        read_only_fields = CAMPOS_SOLO_LECTURA