from django.db import models
from aplicaciones.productos.models import Productos
from aplicaciones.users.models import Restaurantes
from django.utils import timezone
# Create your models here.
class Platos(models.Model):
    nombre_plato = models.CharField(max_length=50, null=False, blank=False)
    descripcion_plato = models.TextField()
    precio = models.IntegerField()
    ingresado_en = models.DateTimeField(auto_now_add=True)
    actualizado_en = models.DateTimeField(auto_now=True)
    fk_restaurante = models.ForeignKey(Restaurantes, on_delete = models.CASCADE, default ="1")

#Tabla de muchos a muchos donde se relacionan platos con productos
class Platos_productos(models.Model):
    fk_plato = models.ForeignKey(Platos, blank=False, null = False, on_delete = models.CASCADE)
    fk_producto = models.ForeignKey(Productos, blank=False, null = False, on_delete = models.CASCADE)
    fk_restaurante = models.ForeignKey(Restaurantes, blank=False, null = False, on_delete = models.CASCADE)
    #Debo configurar correctamente el archivo de javascript que accede a las APIS de platos y productos para que cuando se envie
    #la id del plato no devuelva la id de el registro sino que se filtre el plato
    #antes como la tabla era creada automaticamente se entendia que la id era del plato pero ahora debo configurarla manualmente.

        # Optionally, define a custom primary key field if needed
        # primary_key_field = models.CharField(max_length=100, primary_key=True)



