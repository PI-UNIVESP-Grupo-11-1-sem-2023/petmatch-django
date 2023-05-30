from django.db import models

class participantes(models.Model):
    Nome = models.TextField()
    CPF = models.TextField()
    Telefone = models.TextField()
    Email = models.TextField()
    Cep = models.TextField()
    Rua = models.TextField()
    Cidade = models.TextField()
    Estado = models.TextField()

    def __str__(self):
        return self.Nome