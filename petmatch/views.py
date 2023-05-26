from django.shortcuts import render
from django.http import Http404
from .models import Pet, ONG
import random

def lista_ong(request):
    ongs = ONG.objects.all()
    return render(request, 'petmatch/lista_ongs.html', {"ongs": ongs})

def cadastro_enviado(request):
    return render(request,'petmatch/cadastro-ong-enviado.html')

def login(request):
    return render(request, 'petmatch/login-ong.html')

def index(request):
    #fazendo graça: cada hora aparece numa ordem :)
    pets = list(Pet.objects.all()[0:3])
    random.shuffle(pets)
    return render(request, 'petmatch/index.html', {"pets": pets})

def cadastro_pet(request):
    return render(request, 'petmatch/cadastro_pet.html')

def pet_enviado(request):
    return render(request, 'petmatch/cadastro_pet_enviado.html')

def detalhes_pet(request, pet_id):
    try:
        pet = Pet.objects.get(pk=pet_id)
    except Pet.DoesNotExist:
        raise Http404("Pet não encontrado")
    return render(request, "petmatch/detalhes_pet.html", {"pet": pet})

def lista_pets(request):
    try:
        pets = Pet.objects.all()
    except Pet.DoesNotExist:
        raise Http404("Pet não encontrado")
    return render(request, "petmatch/lista_pets.html", {"pets": pets})