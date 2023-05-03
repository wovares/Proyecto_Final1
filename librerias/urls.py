from django.urls import path
from . import views

urlpatterns = [
    path('', views.inicio, name='inicio'),
    path('nosotros', views.nosotros, name='nosotros'),
    path('libros', views.libros, name='libros'),
    path('contact/', views.contact, name='contact'),
    path('ver-carrito/', views.ver_carrito, name='ver_carrito'),
    path('agregar-carrito/<int:producto_id>/', views.agregar_carrito, name='agregar_carrito'),
    
]