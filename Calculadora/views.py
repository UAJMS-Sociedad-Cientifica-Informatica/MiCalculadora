from builtins import print

from django.http import JsonResponse
from django.shortcuts import render


def calculadora(request):
    template = "calculadora.html"
    return render(request, template)


def calcular(request, texto):
    texto =texto.replace("d", '/')
    return JsonResponse({"resultado": texto}, safe=False)