from django.contrib import admin
from .models import Registro, Casa, Usuario

# Register your models here.

@admin.register(Registro)
class RegistroAdmin(admin.ModelAdmin):
    list_display = ["data", "casa", "consumo", "injecao", "oficial"]
    search_fields = ["casa"]
    list_per_page = 10
    autocomplete_fields = ["casa"]
    date_hierarchy = "data"
    # list_editable = ['oficial', 'consumo', 'injecao']

@admin.register(Casa)
class CasaAdmin(admin.ModelAdmin):
    list_display = ["proprietario","numero", "bairro"]
    search_fields = ["numero"]    
    list_per_page = 10
    autocomplete_fields = ["proprietario"]

@admin.register(Usuario)
class UsuarioAdmin(admin.ModelAdmin):
    list_display = ["nome","email", "telefone", "cpf"]
    search_fields = ["cpf"]
    list_per_page = 10