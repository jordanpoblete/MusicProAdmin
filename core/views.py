from .servicios import get_productos
from .servicios import get_pedidos
from .servicios import post_productos
from .servicios import put_productos
from .servicios import delete_productos
from .servicios import usoAPI
from .forms import ProductosForm
from core.serializers import productoSerializer
from django.http import HttpResponse
from django.shortcuts import render, redirect


def index(request):
     return render(request, 'core/index.html')

# API USD:
def usandoAPI(request):
    context = {
        'apiDolar': usoAPI()
    }
    return render(request, 'core/apiUsd.html', context)

#OBTENERTODO

def get_all(request):
    context = {
        'lista' : get_productos()  
    }          
    return render(request, 'core/get.html', context)

def get_all2(request):
    context = {
        'pedido' : get_pedidos()  
    }          
    return render(request, 'core/get2.html', context)




#METODO POST
def validate(request):
  
    return render(request, 'core/validate.html')

def validate_post(request):
    if request.method == 'POST':
        id_producto  = request.POST["idproducto"]
        imagen  = request.POST["imagen1"]
        nombre  = request.POST["nombre1"]
        descripcion  = request.POST["descripcion1"]
        precio  = request.POST["precio1"]
        disponible  = request.POST["disponible1"]
        TIPO_PRODUCTO_id  = request.POST["tipoproducto"]
        dato = {
            'accion':1,
            'id_producto':id_producto,
            'imagen':imagen,
            'nombre':nombre,
            'descripcion':descripcion,
            'precio':precio,
            'disponible':disponible,
            'TIPO_PRODUCTO_id':TIPO_PRODUCTO_id
        }
        print(dato)
        context = {
            'mensaje': post_productos(dato)
        }
        #return render(request, 'core/guardo.html', context)
        return redirect('get_all')        


#METODO PUT

def validateput(request):
  
    return render(request, 'core/validateput.html')

def validate_put(request):
    if request.method == 'POST':
        id_producto  = request.POST["idproducto"]
        imagen  = request.POST["imagen1"]
        nombre  = request.POST["nombre1"]
        descripcion  = request.POST["descripcion1"]
        precio  = request.POST["precio1"]
        disponible  = request.POST["disponible1"]
        TIPO_PRODUCTO_id  = request.POST["tipoproducto"]
        dato = {
            'id_producto':id_producto,
            'imagen':imagen,
            'nombre':nombre,
            'descripcion':descripcion,
            'precio':precio,
            'disponible':disponible,
            'TIPO_PRODUCTO_id':TIPO_PRODUCTO_id
        }
        print(dato)

        put_productos(dato)

        #return render(request, 'core/guardo.html', context)
        return redirect('get_all')        


   

def delete_producto(request, pk):
    id = pk
    dato = {
        'accion': 69,
        'id_producto': int(id)
    }
    print(dato)
    delete_productos(dato)

    return redirect('get_all')