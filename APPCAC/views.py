from django.shortcuts import render

def inicio(request):
    return render(request, 'index.html')

def preguntas_frecuentes(request):
    return render(request, 'ayuda.html')

def about_us(request):
    return render(request, 'about_us.html')

def animation(request):
    return render(request, 'animation.html')