from django.db import models
from aplicaciones.users.models import Restaurantes
# Create your models here.
class  Productos(models.Model):
    nombre_producto = models.CharField(max_length=50, null=False, blank=False)
    precio_producto = models.IntegerField()
    distribuidor_producto = models.CharField(max_length=50, null=False, blank=False)
    descripcion_producto = models.TextField(null=False, blank=False)
    stock = models.IntegerField(default=10)
    ingresado_en = models.DateTimeField(auto_now_add=True, null=True, blank=True)
    vence_en = models.DateField(auto_now = True)
    fk_restaurante = models.ForeignKey(Restaurantes, on_delete=models.CASCADE, default="1")
