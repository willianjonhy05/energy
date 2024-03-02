from .models import Casa, Registro
from django.forms import ModelForm

class CasaForm(ModelForm):
    class Meta:
        model = Casa
        fields = '__all__'

class RegistroForm(ModelForm):
    class Meta:
        model = Registro
        fields = '__all__'


class AtualizarRegistro(ModelForm):
    class Meta:
        model = Registro
        fields = ['data', 'autor', 'consumo', 'injecao', 'oficial', 'capacidade_maxima']


class RegistroFormCasa(ModelForm):
    class Meta:
        model = Registro
        fields = ['data', 'autor', 'consumo', 'injecao', 'oficial', 'capacidade_maxima']