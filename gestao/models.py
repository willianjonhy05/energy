from django.db import models

class Casa(models.Model):
    rua = models.CharField('Rua', max_length=255, blank=True, null=True)
    numero = models.CharField('Número', max_length=10, blank=True, null=True)
    bairro = models.CharField('Bairro', max_length=20, blank=True, null=True)
    cep = models.CharField('CEP', max_length=9, blank=True, null=True)
    titular = models.CharField('Titular da Casa', max_length=100)
    contrato = models.CharField('Contrato com Distribuidora', max_length=20, blank=True, null=True)
   

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

    def __str__(self):
        return self.data.strftime('%d/%m/%Y')
    
    class Meta:
        verbose_name = "Registro"
        verbose_name_plural = "Registros"






