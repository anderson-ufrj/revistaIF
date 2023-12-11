

from django import forms
from .models import Artigo

# inicializando um formulario para os livros
class ArtigoForm(forms.ModelForm):
    class Meta:
        # modelo referente: Book
        model = Artigo
        # atribuindo todos os campos do modelo Book ao Form
        fields = '__all__'




