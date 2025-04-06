from django.db import models
from .choices import roles, titulos, estado_restaurante
from django.contrib.auth.models import AbstractUser
# Create your models here

class Restaurantes(models.Model):
    numero_identificacion_tributaria = models.BigIntegerField(blank = False, null = False, unique=True)
    rues = models.CharField(max_length=100, blank = False, null = False, unique=True) #Registro Unico Empresarial y Social
    contraseña_restaurante = models.CharField(max_length=100, blank = False, null = False, unique=True)
    direccion_restaurante = models.TextField(blank = False, null = False)
    tipo_restaurante = models.TextField(max_length=100, blank = False, null = False)
    estado = models.CharField(max_length=40, choices = estado_restaurante)
    cedula_propietario = models.IntegerField(unique = True)

class Roles(models.Model):
    nombre_rol = models.CharField(max_length=40, choices=roles)
    fk_restaurante = models.ForeignKey(Restaurantes, on_delete=models.CASCADE, default="1")

    def __str__(self):
        return self.nombre_rol
class Users(AbstractUser):
    fk_rol = models.ForeignKey(Roles, on_delete=models.CASCADE, null=False, blank = False)
    fk_restaurante = models.ForeignKey(Restaurantes, on_delete=models.CASCADE, default="1")

