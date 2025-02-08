from django.contrib import admin
from.models import Texto, Comentarios

class OpcaoInline(admin.TabularInline):
    model = Texto
        
@admin.register(Texto)
class TextoAdmin(admin.ModelAdmin):
    inlines = [OpcaoInline]
    list_display = ['titulo','conteudo', 'data_publicacao']

@admin.register(Comentarios)
class ComentariosAdmin(admin.ModelAdmin):
    list_display = ['comentario', 'data de publicacao']

