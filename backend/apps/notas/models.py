from django.db import models
from apps.usuarios.models import User

# Create your models here.

class Notas(models.Model):
    user = models.ForeignKey(
        User,
        default="",
        null=False,
        on_delete=models.CASCADE
    )
    evento = models.CharField(
        max_length=30,
    )
    fecha = models.DateTimeField(
        verbose_name='Fecha'
    )
    fecha_creacion = models.DateField(
        auto_now_add=True,
        verbose_name='Fecha de creación'
    )

    class Meta:
        verbose_name = 'Evento'
        verbose_name_plural = 'Eventos'
    
    def __str__(self):
        return f'{self.evento} {self.fecha}'