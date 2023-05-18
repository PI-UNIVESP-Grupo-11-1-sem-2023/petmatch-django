from django.shortcuts import render

def cadastro_ong(request):
    return render(request, 'petmatch/cadastro-ong.html')

def cadastro_enviado(request):
    return render(request,'petmatch/cadastro-ong-enviado.html')

def login(request):
    return render(request, 'petmatch/login-ong.html')

def index(request):
    return render(request, 'petmatch/index.html')

def cadastro_pet(request):
    return render(request, 'petmatch/cadastro_pet.html')

def pet_enviado(request):
    return render(request, 'petmatch/cadastro_pet_enviado.html')