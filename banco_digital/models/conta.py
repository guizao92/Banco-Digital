from tkinter import CASCADE
from django.db import models
from banco_digital.models.cliente import Cliente

class Conta(models.Model):
    id_conta = models.AutoField(primary_key= True)
    saldo = models.FloatField(default= 0.0)
    cliente_id = models.ForeignKey(Cliente, on_delete=models.CASCADE)

    def __str__(self) -> str:
        return str(self.id_conta)