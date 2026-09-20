from django.db import models

from config.models import BaseModel


class Cliente(BaseModel):
    nit = models.CharField(max_length=20, unique=True)
    nombre = models.CharField(max_length=120)
    correo = models.EmailField(blank=True)
    telefono = models.CharField(max_length=20)
    limite_credito = models.DecimalField(
        max_digits=10,
        decimal_places=2,
        default=0,
    )
    sitio_web = models.URLField(blank=True)
    activo = models.BooleanField(default=True)

    def __str__(self):
        return self.nombre


class Direccion(BaseModel):
    cliente = models.ForeignKey(
        Cliente,
        on_delete=models.CASCADE,
        related_name="direcciones",
    )
    detalle = models.TextField()
    municipio = models.CharField(max_length=80)
    departamento = models.CharField(max_length=80)
    codigo_postal = models.CharField(max_length=10, blank=True)
    principal = models.BooleanField(default=False)

    def __str__(self):
        return f"{self.cliente.nombre} - {self.municipio}"


class Contacto(BaseModel):
    cliente = models.ForeignKey(
        Cliente,
        on_delete=models.CASCADE,
        related_name="contactos",
    )
    nombre = models.CharField(max_length=100)
    puesto = models.CharField(max_length=80, blank=True)
    telefono = models.CharField(max_length=20)
    correo = models.EmailField(blank=True)
    horario_contacto = models.TimeField(null=True, blank=True)

    def __str__(self):
        return self.nombre