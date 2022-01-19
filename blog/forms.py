from socket import fromshare
from django import forms

class PostFormulario(forms.Form):
   name = forms.CharField(max_length=40)
    # contenido = forms.TextField()
    # fecha_publicacion = forms.DateTimeField(auto_now_add=True)
    # fecha_edicion = forms.DateTimeField(auto_now=True) 

