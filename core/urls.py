from django.urls import path
from .views import index
from . import views

urlpatterns = [
    path('', views.get_all, name='get_all'),
    path('pedidos', views.get_all2, name='get_all2'),
    path('usoAPI', views.usandoAPI, name='usoAPI'),
    path('validate', views.validate, name = 'validate'),
    path('validate_post', views.validate_post, name = 'validate_post'),    
    path('validateput', views.validateput, name = 'validateput'),
    path('validate_put', views.validate_put, name = 'validate_put'),
    path('delete_producto/<pk>/', views.delete_producto, name="delete_producto"),
]