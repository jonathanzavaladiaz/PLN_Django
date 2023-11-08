from django.urls import path
from . import views

urlpatterns = [
    path('', views.inicio, name="inicio"),
    path('agente', views.agente, name="agente"),
    path('procesar_audio/', views.procesar_audio, name='procesar_audio')

]
