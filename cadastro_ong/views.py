from django.shortcuts import render
from cadastro_ong.models import participantes
from django.utils.datastructures import MultiValueDictKeyError
from django.http import HttpResponse
from django.http import QueryDict
from django.views.decorators.clickjacking import xframe_options_exempt
from petmatch.models import Pet, ONG
from petmatch.views import lista_pets
import random





def login(request):

    context = {}


    if request.method == 'POST':

        erros = {}

        Usuario = request.POST.get('Usuario')
        Senha = request.POST.get('Senha')
        if Usuario != "matilhadaba" "lartemporariox" :
            erros['Usuario'] = "Usuário Inválido"
        if Senha != "123456" "xxxx" :
            erros['Senha'] = "Senha Inválida"
            if Usuario == 'matilhadaba':
                return render(request, 'cadastro_ong/pets-matilhadaba.html')
            if Usuario == 'lartemporariox':
                return render(request, 'cadastro_ong/pets-demonstracao.html')
        
        if erros:
            context['erros'] = erros
            context['Usuario'] = Usuario
            context['Senha'] = Senha

  
    return render(request, 'cadastro_ong/login-ong.html', context=context)


def cadastro_ong(request):
    a = 0
    if request.method == 'POST':
        Nome = "Nome" in request.POST and request.POST.get("Nome")
        CPF = 'CPF' in request.POST and request.POST['CPF']
        Telefone = 'Telefone' in request.POST and request.POST['Telefone']
        Email = 'Email' in request.POST and request.POST['Email']
        Cep = 'Cep' in request.POST and request.POST['Cep']
        Rua = 'Rua' in request.POST and request.POST['Rua']
        Cidade = 'Cidade' in request.POST and request.POST['Cidade']
        Estado = 'Estado' in request.POST and request.POST['Estado']
    
        Cadastro_ong = participantes.objects.create(Nome=Nome,CPF=CPF,Telefone=Telefone,Email=Email,Cep=Cep,Rua=Rua,Cidade=Cidade,Estado=Estado)
        form = participantes(request.POST)
        Cadastro_ong.save()

        a = a + 1

        if a > 0:
            return render(request, 'cadastro_ong/cadastro-ong-enviado.html')

    return render(request, 'cadastro_ong/cadastro-ong.html')


def cadastro_enviado(request):
    return render(request, 'cadastro_ong/cadastro-ong-enviado.html/')

def pets_matilhadaba(request):
    return render(request, 'cadastro_ong/pets-matilhadaba.html', )

def pets_lartemporariox(request):
    return render(request,'cadastro_ong/pets-demonstracao.html')