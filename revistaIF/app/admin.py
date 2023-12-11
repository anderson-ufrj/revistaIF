from django.contrib import admin
from app.models import *
from .forms import *

# classe para exibir os livros inline: direto na interface que exibe o autor
class ArtigoInline(admin.TabularInline):  # ou admin.StackedInline que mostraria a exibição inline empilhada
    # model referente: Book
    model = Artigo
    # form referente: BookForm
    form = ArtigoForm
    extra = 1  # numero de formularios vazios a serem exibidos

# classe para exibir os autores
class UsuarioAdmin(admin.ModelAdmin):
    # atributo inline para exibir os livros inline xD
    inlines = [ArtigoInline]


admin.site.register(Curso)
admin.site.register(Tipo)
admin.site.register(Periodo)
admin.site.register(Usuario,UsuarioAdmin)
admin.site.register(TipoArtigo)
admin.site.register(Artigo)