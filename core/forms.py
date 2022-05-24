from django import forms
from django.forms import ModelForm
from .models import producto



class ProductosForm(ModelForm):

    class Meta:
        model = producto
        fields = ['id_producto','imagen','nombre','descripcion','precio','disponible','TIPO_PRODUCTO_id']

