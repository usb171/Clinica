from django.urls import path
from .views import agenda, carregarAgendaAjax, buscarAgendaAjax


urlpatterns = [
    path('agenda', agenda, name='agenda'),
    path('carregarAgendaAjax', carregarAgendaAjax, name='carregarAgendaAjax'),
    path('buscarAgendaAjax', buscarAgendaAjax, name='buscarAgendaAjax'),
]