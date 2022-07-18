from rest_framework import serializers
from banco_digital.models.conta import Conta


class ListaContasClienteSerializer(serializers.ModelSerializer):
    cliente = serializers.ReadOnlyField(source='cliente.id_cliente')

    class Meta:
        model = Conta
        fields = ['cliente', 'id_conta', 'saldo']


        
