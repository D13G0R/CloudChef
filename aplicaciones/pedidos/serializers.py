from rest_framework import serializers
from .models import plato_producto
class plato_productoSerializer(serializers.ModelSerializer):
    class Meta:
        model = plato_producto
        fields = ('__all__')