from rest_framework import serializers
from banco_digital.execptions.conta_inexistente_error import ContaInexistenteError
from banco_digital.models.conta import Conta


class ConsultaSaldoContaSerializer(serializers.ModelSerializer):
    conta = serializers.ReadOnlyField(source='conta.id_conta')

    class Meta:
        model = Conta
        fields = ['conta', 'saldo']
