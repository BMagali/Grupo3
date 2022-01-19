from django.urls import path
from django.urls.conf import include
from blog import views as v

urlpatterns = [
    path('', v.inicio ),
    path('post/', v.posts, name="Post" ),
    path('ShowPost/<id>', v.ShowPost, name="ShowPost"),
    path('comentario/<id>', v.comentario, name="comentario"),
    path('tagFormulario/', v.tagFormulario, name="TagFormulario"),
    path('busquedaTag/', v.busquedaTag, name='busquedaTag'),
    path('buscar/', v.buscar, name='Buscar'),
]
