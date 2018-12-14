from django.shortcuts import render
from usuario.models import Usuario

def usuarios(request):
    if request.method == 'GET':
        contexto = {'usuarios': Usuario.objects.all()}
        print(contexto)
        return render(request, 'usuario/usuarios.html', contexto)

