from django.db import models
from django.db.models import CharField, IntegerField


class Calcular(models.Model):
    funcion = CharField(max_length=200)
    resultado = IntegerField(default=0)
    fecha_de_creacion = models.DateField(auto_now_add=True)