from django.contrib import admin

from blog.models import Comentario, Like, Post, Tag

admin.site.register(Tag)
admin.site.register(Post)
admin.site.register(Comentario)
admin.site.register(Like)
