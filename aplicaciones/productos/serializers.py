from rest_framework import serializers
from .models import Productos

class ProductoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Productos
        fields = ['id', 'nombre_producto', 'descripcion_producto', 'precio_producto']
