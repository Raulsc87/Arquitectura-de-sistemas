from django.db import models

from config.models import BaseModel


class Proveedor(BaseModel):
    nit = models.CharField(max_length=20, unique=True)
    nombre = models.CharField(max_length=120)
    correo = models.EmailField(blank=True)
    telefono = models.CharField(max_length=20)
    dias_credito = models.IntegerField(default=0)
    calificacion = models.FloatField(default=0)
    activo = models.BooleanField(default=True)

    def __str__(self):
        return self.nombre


class Compra(BaseModel):
    ESTADOS = [
        ("solicitada", "Solicitada"),
        ("recibida", "Recibida"),
        ("cancelada", "Cancelada"),
    ]

    proveedor = models.ForeignKey(
        Proveedor,
        on_delete=models.PROTECT,
        related_name="compras",
    )
    usuario = models.ForeignKey(
        "usuarios.Usuario",
        on_delete=models.PROTECT,
        related_name="compras",
    )
    numero_orden = models.CharField(max_length=30, unique=True)
    fecha_compra = models.DateTimeField()
    total = models.DecimalField(
        max_digits=12,
        decimal_places=2,
        default=0,
    )
    estado = models.CharField(
        max_length=20,
        choices=ESTADOS,
        default="solicitada",
    )

    def __str__(self):
        return self.numero_orden


class DetalleCompra(BaseModel):
    compra = models.ForeignKey(
        Compra,
        on_delete=models.CASCADE,
        related_name="detalles",
    )
    producto = models.ForeignKey(
        "productos.Producto",
        on_delete=models.PROTECT,
        related_name="detalles_compra",
    )
    cantidad = models.PositiveIntegerField()
    costo_unitario = models.DecimalField(
        max_digits=10,
        decimal_places=2,
    )
    lote = models.CharField(max_length=50, blank=True)
    fecha_vencimiento = models.DateField(null=True, blank=True)

    def __str__(self):
        return f"{self.producto.nombre} x {self.cantidad}"