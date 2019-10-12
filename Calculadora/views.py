from builtins import print

from django.http import JsonResponse
from django.shortcuts import render

from Calculadora.models import Calcular, FormularioCalculadora, FormularioEstudiante


def calculadora(request):
    template = "calculadora.html"
    data = {'titulo': "Mi Calculadora ",
            "lista": [1, 2, 5],
            "si": False,
            }
    return render(request, template, data)

def mi_formulario(request):
    template = "formulario.html"
    formulario = FormularioCalculadora(request.POST or None)
    calculados = Calcular.objects.filter(funcion="5+5")
    estudiante = FormularioEstudiante(request.POST or None)
    data = {
        'titulo': 'Formulario',
        'formulario': formulario,
        'calculados': calculados,
        'estudiante': estudiante,
            }
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

    return JsonResponse({"resultado": resultado, "resultado2": resultado, "resultado3": resultado}, safe=False)