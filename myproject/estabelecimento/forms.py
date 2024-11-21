from django import forms
from .models import Estabelecimento

class EstabelecimentoForm(forms.ModelForm):
    class Meta:
        model = Estabelecimento
        fields = ['nome', 'telefone', 'descricao', 'foto_local', 'media_avaliacao', 'proprietario', 'endereco', 'lat', 'lng', 'categoria']
