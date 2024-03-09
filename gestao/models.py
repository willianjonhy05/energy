from django.db import models
from datetime import date
from django.contrib.auth import get_user_model

class Usuario(models.Model):
    nome = models.CharField('Nome', max_length=255)
    data_nasc = models.DateField('Data de Nascimento', null=True, blank=True)
    foto = models.ImageField("Foto", upload_to='avatares', blank=True, null=True)
    email = models.EmailField('E-mail')
    telefone = models.CharField("Telefone", max_length=15, null=True, blank=True)
    cpf = models.CharField("CPF", max_length=15, null=True, blank=True)
    user = models.OneToOneField(get_user_model(), verbose_name="Usuário",on_delete=models.CASCADE, null=True, blank=True, related_name="autor")

    @property
    def idade(self):
        hoje = date.today()
        diferenca = hoje - self.data_nasc
        return round(diferenca.days // 365.25)    

    def __str__(self):
       return self.nome
    
    class Meta:
        verbose_name = "Usuario"
        verbose_name_plural = "Usuarios"    

class Casa(models.Model):
    rua = models.CharField('Rua', max_length=255, blank=True, null=True)
    numero = models.CharField('Número', max_length=10, blank=True, null=True)
    bairro = models.CharField('Bairro', max_length=20, blank=True, null=True)
    cep = models.CharField('CEP', max_length=9, blank=True, null=True)
    titular = models.CharField('Titular da Casa', max_length=100)
    contrato = models.CharField('Contrato com Distribuidora', max_length=20, blank=True, null=True)
    proprietario = models.ForeignKey(Usuario, on_delete=models.CASCADE, verbose_name="Titular", related_name="titular", blank=True, null=True)   

    def __str__(self):
       return f"Casa {self.numero}"
    
    class Meta:
        verbose_name = "Casa"
        verbose_name_plural = "Casas"


class Registro(models.Model):
    data = models.DateField("Data do Registro")
    autor = models.CharField("Autor do Registro", max_length=50)
    consumo = models.IntegerField('03')
    injecao = models.IntegerField('103')
    oficial = models.BooleanField("Captado pela Distribuidora", default=False)
    casa = models.ForeignKey(Casa, verbose_name="Casa", on_delete=models.CASCADE, related_name="casas")
    capacidade_maxima = models.IntegerField('Capacidade Máxima de Produção Solar', default=600)
    
    @property
    def saldo_parcial(self):
        return self.injecao - self.consumo

    def __str__(self):
        return self.data.strftime('%d/%m/%Y')
    
    class Meta:
        verbose_name = "Registro"
        verbose_name_plural = "Registros"






