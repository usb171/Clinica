from django.urls import path
from .views import paciente


urlpatterns = [
    path('meusPacientes', paciente, name='meusPacientes'),
]