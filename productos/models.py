from django.db import models

from config.models import BaseModel


class Categoria(BaseModel):
    nombre = models.CharField(max_length=80, unique=True)
    descripcion = models.TextField(blank=True)
    activa = models.BooleanField(default=True)

    def __str__(self):
        return self.nombre


class Producto(BaseModel):
    categoria = models.ForeignKey(
        Categoria,
        on_delete=models.PROTECT,
        related_name="productos",
    )
    codigo = models.CharField(max_length=30, unique=True)
    nombre = models.CharField(max_length=120)
    descripcion = models.TextField(blank=True)
    precio = models.DecimalField(max_digits=12, decimal_places=2)
    peso_kg = models.FloatField(default=0)
    fecha_vencimiento = models.DateField(null=True, blank=True)
    disponible = models.BooleanField(default=True)

    def __str__(self):
        return self.nombre


class Inventario(BaseModel):
    producto = models.OneToOneField(
        Producto,
        on_delete=models.CASCADE,
        related_name="inventario",
    )
    cantidad = models.PositiveIntegerField(default=0)
    stock_minimo = models.PositiveIntegerField(default=5)
    stock_maximo = models.PositiveIntegerField(default=100)
    ubicacion = models.CharField(max_length=100)
    ultima_entrada = models.DateTimeField(null=True, blank=True)

    def __str__(self):
        return f"{self.producto.nombre}: {self.cantidad}"