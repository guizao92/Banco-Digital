from datetime import date
from tkinter import CASCADE
from django.db import models
from banco_digital.models.cliente import Cliente
from banco_digital.models.conta import Conta

class Transferencia(models.Model):
    id_transferencia = models.AutoField(primary_key= True)
    valor_transferencia = models.FloatField()
    data_transferencia = models.DateField(default=date.today) #Data da transferencia será automaticamente a do dia
    conta_entrada = models.ForeignKey(Conta, on_delete=models.PROTECT, related_name='conta_entrada') 
    conta_saida = models.ForeignKey(Conta, on_delete=models.PROTECT, related_name='conta_saida')
    #PROTECT faz com que contas e clientes envolvidos em transferências não possam ser excluidos