from builtins import print

from django.http import JsonResponse
from django.shortcuts import render

from Calculadora.models import Calcular


def calculadora(request):
    template = "calculadora.html"
    data = {'dato': "hola mundo"}
    return render(request, template, data)


def calcular(request, texto):
    texto =texto.replace("d", '/')
    resultado = 10

    # ============ Cargar datos ================
    calcular = Calcular()
    calcular.funcion = texto
    calcular.resultado = resultado
    calcular.save()
    # =========================================

    # ============ Sacar datos ================
    calcular = Calcular.objects.all()
    for i in calcular:
        print(i.funcion)
        print(i.resultado)
        print("======")
    # ========================================

    return JsonResponse({"resultado": resultado}, safe=False)