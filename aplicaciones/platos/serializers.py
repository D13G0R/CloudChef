from rest_framework import serializers
from .models import Platos, Platos_productos

class PlatosSerializer (serializers.ModelSerializer):
    class Meta:
        model = Platos
        fields = ("id", "nombre_plato", "precio")

class PlatosProductosSerializer(serializers.ModelSerializer):
    class Meta:
        model = Platos_productos
        fields = ("fk_plato", "fk_producto")