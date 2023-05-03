from django import forms

class CompraForm(forms.Form):
    nombre = forms.CharField(max_length=100)
    apellido = forms.CharField(max_length=100)
    correo = forms.EmailField()
    aceptar_condiciones = forms.BooleanField(required=True)