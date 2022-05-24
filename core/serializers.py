from rest_framework import serializers
from core.models import producto

class productoSerializer(serializers.ModelSerializer):
    class Meta:
        model = producto
        fields = ['id_producto', 'imagen', 'nombre', 'descripcion','precio', 'disponible','TIPO_PRODUCTO_id']

