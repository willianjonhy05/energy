from .models import Casa, Registro
from django.forms import ModelForm, EmailField, CharField
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import get_user_model


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


class RegistrationForm(UserCreationForm):

    first_name = CharField(max_length=150, label="Nome")
    last_name = CharField(max_length=150, label="Sobrenome")
    email = EmailField(max_length=200, label="Email")
    
    class Meta:
        model = get_user_model()
        fields=['username', 'first_name', 'last_name', 'email', 'password1', 'password2' ]