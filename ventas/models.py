from django.db import models

from config.models import BaseModel


class Venta(BaseModel):
    ESTADOS = [
        ("pendiente", "Pendiente"),
        ("pagada", "Pagada"),
        ("cancelada", "Cancelada"),
    ]

    cliente = models.ForeignKey(
        "clientes.Cliente",
        on_delete=models.PROTECT,
        related_name="ventas",
    )
    usuario = models.ForeignKey(
        "usuarios.Usuario",
        on_delete=models.PROTECT,
        related_name="ventas",
    )
    numero_factura = models.PositiveBigIntegerField(unique=True)
    total = models.DecimalField(
        max_digits=12,
        decimal_places=2,
        default=0,
    )
    estado = models.CharField(
        max_length=20,
        choices=ESTADOS,
        default="pendiente",
    )
    fecha_entrega = models.DateField(null=True, blank=True)
    observaciones = models.TextField(blank=True)

    def __str__(self):
        return f"Venta {self.numero_factura}"


class DetalleVenta(BaseModel):
    venta = models.ForeignKey(
        Venta,
        on_delete=models.CASCADE,
        related_name="detalles",
    )
    producto = models.ForeignKey(
        "productos.Producto",
        on_delete=models.PROTECT,
        related_name="detalles_venta",
    )
    cantidad = models.PositiveIntegerField()
    precio_unitario = models.DecimalField(
        max_digits=10,
        decimal_places=2,
    )
    descuento = models.FloatField(default=0)

    def __str__(self):
        return f"{self.producto.nombre} x {self.cantidad}"


class Pago(BaseModel):
    METODOS = [
        ("efectivo", "Efectivo"),
        ("tarjeta", "Tarjeta"),
        ("transferencia", "Transferencia"),
    ]

    venta = models.ForeignKey(
        Venta,
        on_delete=models.CASCADE,
        related_name="pagos",
    )
    metodo = models.CharField(max_length=20, choices=METODOS)
    monto = models.DecimalField(max_digits=12, decimal_places=2)
    fecha_pago = models.DateTimeField()
    confirmado = models.BooleanField(default=False)
    referencia = models.CharField(max_length=100, blank=True)
    datos_adicionales = models.JSONField(default=dict, blank=True)

    def __str__(self):
        return f"Pago de {self.monto}"