from django.urls import path,include
from APPCAC.views import *

urlpatterns = [
    path('',inicio, name='Index'),
]