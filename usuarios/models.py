from django.db import models

from config.models import BaseModel


class Permiso(BaseModel):
    codigo = models.CharField(max_length=50, unique=True)
    descripcion = models.TextField()
    nivel = models.PositiveSmallIntegerField(default=1)

    def __str__(self):
        return self.codigo


class Rol(BaseModel):
    nombre = models.CharField(max_length=50, unique=True)
    descripcion = models.TextField(blank=True)
    activo = models.BooleanField(default=True)
    permisos = models.ManyToManyField(
        Permiso,
        blank=True,
        related_name="roles",
    )

    def __str__(self):
        return self.nombre


class Usuario(BaseModel):
    rol = models.ForeignKey(
        Rol,
        on_delete=models.PROTECT,
        related_name="usuarios",
    )
    nombre = models.CharField(max_length=100)
    correo = models.EmailField(unique=True)
    telefono = models.CharField(max_length=20, blank=True)
    fecha_nacimiento = models.DateField(null=True, blank=True)
    activo = models.BooleanField(default=True)

    def __str__(self):
        return self.nombre