from django.db import models
from django.utils import timezone

class Wunsch(models.Model):
    Texto = models.CharField(max_length = 500)
    data_publicacao = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return self.Texto

class Opcao(models.Model):
    Wunsch = models.ForeignKey(Texto , on_delete=models.CASCADE, related_name='opcoes')
    texto_opcao = models.CharField(max_length=100)
    
    def __str__(self):
        return self.texto_opcao
