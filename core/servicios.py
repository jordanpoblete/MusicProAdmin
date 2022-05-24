import json
import requests

def usoAPI():
    url = 'https://api.cmfchile.cl/api-sbifv3/recursos_api/dolar/2022/05?apikey=71431b71f89b61312bcfa6c9a5efebd295273d77&formato=json'
    r = requests.get(url)
    datos = r.json()
    return datos

def get_productos():
    url = 'https://webservicejoldan.herokuapp.com/controller/producto.php?REQUEST_METHOD=GET'
    resultado = requests.get(url)
    contactos = resultado.json()
    return contactos

def get_pedidos():
    url = 'https://webservicejoldan.herokuapp.com/controller/producto.php?REQUEST_METHOD=GET'
    resultado = requests.get(url)
    pedidos = resultado.json()
    return pedidos


def post_productos(dato):
    url = 'https://webservicejoldan.herokuapp.com/controller/producto.php?REQUEST_METHOD=POST'
    respuesta = requests.post(url, json = dato)
    return respuesta


def put_productos(dato):
    url = 'https://webservicejoldan.herokuapp.com/controller/producto.php?REQUEST_METHOD=PUT'
    respuesta = requests.put(url, json = dato)
    return respuesta    


def delete_productos(dato):
    url = 'https://webservicejoldan.herokuapp.com/controller/producto.php??REQUEST_METHOD=PEPE'
    respuesta = requests.post(url, json = dato)
    return respuesta   