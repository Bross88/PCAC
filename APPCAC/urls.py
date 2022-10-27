from django.urls import path,include
from APPCAC.views import inicio,preguntas_frecuentes,about_us,animation,formulario,destinos,error


urlpatterns = [
    path('',inicio, name='Index'),
    path('preguntas_frecuentes/',preguntas_frecuentes,name= 'APPCACfrecuentes'),
    path('about/',about_us, name='APPCACAboutus'),
    path('animation/',animation, name='APPCACAnimation'),
    path('suscribirse/',formulario, name="APPCACformulario"),
    path('destinos/',destinos, name="APPCACDestinos"), 
    path('error/',error, name="APPCACError"),
]