from django.db import models
from aplicaciones.users.models import Users
from aplicaciones.platos.models import Platos
from aplicaciones.productos.models import Productos
from aplicaciones.users.models import Restaurantes
from .choices import estados

# Create your models here.
class pedidos(models.Model):
    fk_usuario = models.ForeignKey(Users, on_delete=models.CASCADE)
    estado_pedido = models.CharField(max_length=50, choices = estados, default="pendiente")
    pedido_en = models.DateTimeField(auto_now_add=True)
    fk_restaurante = models.ForeignKey(Restaurantes, on_delete=models.CASCADE, default="1")
class plato_producto(models.Model):
    fk_pedido = models.ForeignKey(pedidos, on_delete = models.CASCADE, null = False, blank = False, related_name ="platos_productos")
    fk_plato = models.ForeignKey(Platos, on_delete = models.CASCADE, null = True, blank = True, related_name ="plato_pedido")
    fk_producto = models.ForeignKey(Productos, on_delete = models.CASCADE, null = False, blank = False, related_name ="producto_pedido")
    cantidad = models.IntegerField()
    fk_restaurante = models.ForeignKey(Restaurantes, on_delete=models.CASCADE)
