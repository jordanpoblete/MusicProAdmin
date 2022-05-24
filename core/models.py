from django.db import models

# Create your models here.



class producto(models.Model):
    id_producto = models.IntegerField(primary_key=True, verbose_name='Id producto')
    imagen = models.TextField()
    nombre = models.CharField(max_length=200, verbose_name='Nombre del producto')
    descripcion = models.CharField(max_length=200, verbose_name='Descripcion del producto')
    precio = models.IntegerField(verbose_name='Precio del producto')
    disponible = models.CharField(max_length=1)
    TIPO_PRODUCTO_id = models.IntegerField()

    def __str__(self):
        return self.nombre