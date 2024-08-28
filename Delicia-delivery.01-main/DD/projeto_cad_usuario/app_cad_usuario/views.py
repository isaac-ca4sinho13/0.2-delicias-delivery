from django.shortcuts import render
from .models import Usuarios

def home(request):
    return render(request,'usuarios/home.html')
def usuarios(request):
    novo_usuario = Usuarios()
    novo_usuario.nome = request.POST.get('nome')
    novo_usuario.numero = request.POST.get('numero')
    novo_usuario.senha = request.POST.get('senha')
    novo_usuario.save()

    usuarios = {
        'usuarios': Usuarios.objects.all()
    }
    return render(request, 'usuarios/usuarios.html', usuarios)
