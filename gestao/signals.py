from .models import Usuario
from django.db.models.signals import post_save
from django.dispatch import receiver
from django.contrib.auth import get_user_model



@receiver(post_save, sender=get_user_model())
def create_usuario(sender, instance, created, **kwargs):
    if created:
        usuario = Usuario.objects.create(nome=instance.get_full_name(), email=instance.email, user=instance)
