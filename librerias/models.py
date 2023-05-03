from django.db import models
from django.contrib.auth.models import User



# Create your models here.

class Autor(models.Model):
    nombre = models.CharField(max_length=100)
    apellido = models.CharField(max_length=100)

    def __str__(self):
        return f"{self.nombre} {self.apellido}"

class Libro(models.Model):
    titulo = models.CharField(max_length=200)
    imagen_url = models.CharField(max_length=200,blank=True,null=True)
    precio = models.DecimalField(max_digits=10, decimal_places=2)
    autor = models.ForeignKey(Autor, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.titulo} por {self.autor}"

class Producto(models.Model):
    nombre = models.CharField(max_length=255)
    descripcion = models.TextField()
    precio = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return f"Libro {self.nombre}"


class Carrito(models.Model):
    usuario = models.ForeignKey(User, on_delete=models.CASCADE)
    fecha_creacion = models.DateTimeField(auto_now_add=True)
    fecha_actualizacion = models.DateTimeField(auto_now=True)
    productos = models.ManyToManyField(Producto, through='ProductoCarrito')

    def __str__(self):
        return f'Carrito de {self.usuario.username}'


class ProductoCarrito(models.Model):
    producto = models.ForeignKey(Producto, on_delete=models.CASCADE)
    carrito = models.ForeignKey(Carrito, on_delete=models.CASCADE)
    cantidad = models.PositiveIntegerField(default=1)

    def __str__(self):
        return f'{self.cantidad} {self.producto.nombre} en el carrito de {self.carrito.usuario.username}'