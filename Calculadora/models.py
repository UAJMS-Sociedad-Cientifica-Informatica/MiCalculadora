from django.db import models
from django.db.models import CharField, IntegerField
from django import forms
from django.forms import EmailField


class Calcular(models.Model):
    funcion = CharField(max_length=200)
    resultado = IntegerField(default=0)
    fecha_de_creacion = models.DateField(auto_now_add=True)

class Estudiante(models.Model):
    nombres = CharField(max_length=10)
    ru = IntegerField(unique=True)
    correo = EmailField()


class FormularioCalculadora(forms.ModelForm):
    class Meta:
        model = Calcular
        fields = [
            'funcion',
            'resultado',
        ]

class FormularioEstudiante(forms.ModelForm):
    class Meta:
        model = Estudiante
        fields = [
            'nombres',
            'ru',
        ]
