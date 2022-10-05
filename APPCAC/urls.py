from django.urls import path,include
from APPCAC.views import inicio,preguntas_frecuentes

urlpatterns = [
    path('',inicio, name='Index'),
    path('preguntas_frecuentes/',preguntas_frecuentes,name= 'APPCACfrecuentes')
]