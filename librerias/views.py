from django.shortcuts import render, redirect,get_object_or_404
from django.core.paginator import Paginator
from django.core.mail import send_mail
from django.conf import settings
from .models import Libro,Producto,ProductoCarrito,Carrito
from django.core.mail import EmailMessage
from django.template.loader import render_to_string
from django.contrib import messages
from .forms import CompraForm



# Create your views here.

def inicio(request):
    
    return render(request,"paginas/inicio.html",)

def nosotros(request):
    
    return render(request,"paginas/nosotros.html",)

def libros(request):
    libros = Libro.objects.order_by('titulo').all()

    # Obtener el número de libros por página (5 por defecto, pero se puede cambiar con un parámetro en la URL)
    libros_per_page = request.GET.get('libros_per_page', 5)
    
    # Crear un objeto Paginator con los libros y el número de libros por página
    paginator = Paginator(libros, libros_per_page)

    # Obtener el número de página actual (1 por defecto)
    page = request.GET.get('page', 1)

    # Obtener la lista de libros para la página actual
    libros = paginator.get_page(page)

    # Renderizar la plantilla con la lista de libros y el número de libros por página
    return render(request, 'libros/index.html', {'libros': libros, 'libros_per_page': libros_per_page, 'pagina':page})

def contact(request):
   if request.method == 'POST':
      nombre = request.POST['nombre']
      apellido = request.POST['apellido']
      email = request.POST['email']
      asunto = request.POST['asunto']
      mensaje = request.POST['mensaje']

      template = render_to_string('paginas/email_template.html', {'nombre': nombre,'apellido': apellido, 'email': email, 'mensaje': mensaje})

      email = EmailMessage(asunto, template, settings.EMAIL_HOST_USER, ['williamovares06@gmail.com'])

      email.fail_silently = False
      email.send()

      messages.success(request, 'Tu mensaje ha sido enviado')
      return redirect('inicio')
   else:
       return render(request, 'paginas/contact.html')
    
def ver_carrito(request):
    carrito = Carrito.objects.first()  # Obtener el primer carrito, aquí se debe implementar lógica para obtener el carrito del usuario actual
    productos = carrito.productos.all()
    contexto = {'productos': productos}
    return render(request, 'paginas/carrito.html', contexto)

def agregar_carrito(request, producto_id):
    producto = Producto.objects.get(id=producto_id)
    carrito = Carrito(usuario=request.user)
    carrito.save()
    producto_carrito, created = ProductoCarrito.objects.get_or_create(producto=producto, carrito=carrito)
    producto_carrito.cantidad += 1
    producto_carrito.save()

    return redirect('ver_carrito')

def enviar_correo(request):
    if request.method == 'POST':
        nombre = request.POST.get('nombre')
        apellido = request.POST.get('apellido')
        correo = request.POST.get('correo')
        carrito = request.session.get('carrito', {})
        total = 0
        contenido = ""
        for key, value in carrito.items():
            producto = Producto.objects.get(id=key)
            contenido += f'{value["cantidad"]} {producto.nombre} - ${producto.precio * value["cantidad"]}\n'
            total += float(producto.precio * value["cantidad"])
        # Envío del correo electrónico
        asunto = f'Confirmación de reserva - Total: ${total}'
        mensaje = f'Hola {nombre} {apellido},\n\nGracias por su compra.\n\nDetalles de la compra:\n\n{contenido}\n\nTotal: ${total}\n\nSaludos cordiales,\n\nEl equipo de ventas'
        destinatario = correo
        send_mail(asunto, mensaje, settings.EMAIL_HOST_USER, ['williamovares06@gmail.com'], fail_silently=False)
    
       # Crear carrito en la base de datos
        if request.user.is_authenticated:
           carrito = Carrito(usuario=request.user)
           carrito.save()
           for key, value in request.session['carrito'].items():
               producto = Producto.objects.get(id=key)
               producto_carrito = ProductoCarrito(carrito=carrito, producto=producto, cantidad=value['cantidad'])
               producto_carrito.save()
           del request.session['carrito']
    
    # Redireccionar a la página de agradecimiento
        return redirect('agradecimiento')
    else:
        return redirect('ver_carrito')







