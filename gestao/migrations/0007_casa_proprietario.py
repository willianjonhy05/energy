# Generated by Django 4.2.10 on 2024-03-09 02:16

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('gestao', '0006_usuario_cpf_usuario_foto'),
    ]

    operations = [
        migrations.AddField(
            model_name='casa',
            name='proprietario',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='titular', to='gestao.usuario', verbose_name='Titular'),
        ),
    ]
