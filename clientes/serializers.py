from rest_framework import serializers

from .models import Cliente, Contacto, Direccion


CAMPOS_SOLO_LECTURA = (
    "id",
    "is_deleted",
    "deleted_at",
    "created_at",
    "updated_at",
)


class ClienteSerializer(serializers.ModelSerializer):
    class Meta:
        model = Cliente
        fields = "__all__"
        read_only_fields = CAMPOS_SOLO_LECTURA


class DireccionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Direccion
        fields = "__all__"
        read_only_fields = CAMPOS_SOLO_LECTURA


class ContactoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Contacto
        fields = "__all__"
        read_only_fields = CAMPOS_SOLO_LECTURA