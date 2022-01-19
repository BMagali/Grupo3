from socket import fromshare
from django import forms

class TagFormulario(forms.Form):
   name = forms.CharField(max_length=40)
 

