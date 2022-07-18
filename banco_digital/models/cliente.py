from django.db import models

class Cliente(models.Model):
    id_cliente = models.AutoField(primary_key= True)
    nome = models.CharField(max_length=100)
    cpf = models.CharField(max_length=11, unique=True)
    email = models.CharField(max_length=60)
    telefone = models.CharField(max_length=14)
    endereço = models.CharField(max_length=100)

    def __str__(self) -> str:
        return self.nome