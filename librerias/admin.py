from django.contrib import admin
from .models import Libro,Carrito,Producto,ProductoCarrito

# Register your models here.
admin.site.register(Libro)
admin.site.register(Carrito)
admin.site.register(Producto)
admin.site.register(ProductoCarrito)