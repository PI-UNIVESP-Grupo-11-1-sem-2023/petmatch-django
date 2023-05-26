from django.db import models
from django.utils import timezone
# Create your models here.

# nao esqueca de rodar python manage.py makemigrations petmatch

class Pet(models.Model):
    animal = models.CharField(max_length=200)
    nome = models.CharField(max_length=200)
    data_nascimento = models.DateTimeField("data de nascimento")
    porte = models.CharField(max_length=10) # pequeno / medio / grande
    sexo = models.CharField(max_length=5) # femea / macho
    cor = models.CharField(max_length=200)
    localizacao = models.CharField(max_length=500)
    comportamento = models.CharField(max_length=500)
    email_contato = models.CharField(max_length=500, default="noreply@noreply.com.br")
    foto = models.ImageField(upload_to="photos/")

    def __str__(self):
        return f"""Esse é o {self.animal} de nome {self.nome} 
        nasceu em {self.data_nascimento} de porte {self.porte} 
        cor {self.cor} é {self.sexo}, tem comportamento {self.comportamento} 
        e está localizado em {self.localizacao}"""
    
    def idade(self) -> int:
        return timezone.now().year - self.data_nascimento.year
    

class ONG(models.Model):
    nome = models.CharField(max_length=200)
    cpf_cnpj = models.CharField(max_length=14)
    telefone = models.CharField(max_length=200)
    email= models.CharField(max_length=200)
    cep = models.CharField(max_length=8)
    rua = models.CharField(max_length=200)
    cidade = models.CharField(max_length=200)
    estado = models.CharField(max_length=2)

    def __str__(self):
        return f"""{self.nome} tem {self.cpf_cnpj} e {self.telefone}
        no {self.email} fica localizada no endereço: {self.cep}
        na {self.rua}, {self.cidade} - {self.estado}"""