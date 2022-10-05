from django.shortcuts import render

def inicio(request):
    return render(request, 'index.html')

def preguntas_frecuentes(request):
    return render(request, 'ayuda.html')



