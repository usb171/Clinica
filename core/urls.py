from django.urls import path
from .views import login, dashboard, logout


urlpatterns = [
    path('', login, name='login'),
    path('logout/', logout, name='logout'),
    path('dashboard', dashboard, name='dashboard'),
]