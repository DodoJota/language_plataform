from django import forms
from .models import Topico, Resposta

class TopicoForm(forms.ModelForm):
    class Meta:
        model = Topico
        fields = ['titulo', 'conteudo']

class RespostaForm(forms.ModelForm):
    class Meta:
        model = Resposta
        fields = ['conteudo']
