from django.urls import path
from . import views

app_name = 'encuesta'

urlpatterns = [
    path('', views.index, name='index'),
    path('enviar/', views.enviar, name='enviar'),
    path('operaciones/', views.operaciones, name='operaciones'),
    path('cilindro/', views.cilindro, name='cilindro'),
]
