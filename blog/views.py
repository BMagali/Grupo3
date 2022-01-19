
from http.client import HTTPResponse
from django.shortcuts import render
from blog.forms import PostFormulario
from blog.models import Comentario, Like, Post, Tag, Usuario
from blog.forms import PostFormulario

# def usuario(request,id):
#     usuario=Usuario.objects.get(id=id)
#     return render(request, 'post.html', {"usuario":usuario})

def inicio(request):
    return render(request, 'inicio.html')

def posts(request):
    posts=Post.objects.all()
    return render(request, 'post.html', {"posts":posts})

def postFormulario(request):
    if request.method == 'POST':
        miformulario= PostFormulario(request.POST)
        print(miformulario)
        if miformulario.is_valid:
            informacion= miformulario.cleaned_data
            tag = Tag (nombre=informacion['name'])
            tag.save()

            return render(request,'inicio.html')
    else:
        miformulario= PostFormulario()

    return render(request, "postFormulario.html", {"miformulario":miformulario})

def busquedaTag(request):
    return render(request, 'busquedaTag.html')

def buscar(request):
    respuesta= f"Estoy buscando el tag id numero: {request.GET['name'] }"
    return HTTPResponse(respuesta)


def ShowPost(request,id):
    post=Post.objects.get(id=id)
    tags=Tag.objects.filter(post__id=id)
    return render(request, 'show.html', {"post":post, "tags":tags})

def comentario(request,id):
    comentario=Comentario.objects.get(id=id)
    return render(request, 'comentario.html', {"comentario":comentario})

def like(request,id):
    like=Like.objects.get(id=id)
    return render(request, 'like.html', {"like":like})