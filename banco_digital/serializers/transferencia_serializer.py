from rest_framework import serializers
from banco_digital.models.conta import Conta
from banco_digital.models.transferencia import Transferencia


class TransferenciaSerializer(serializers.HyperlinkedModelSerializer):
        

    class Meta():
        model = Transferencia
        fields = "__all__"
    

    def update(self, instance, validated_data):
            validated_data['conta_entrada']['saldo'] = validated_data['conta_entrada']['saldo']+ validated_data['valor_transferencia']
            validated_data['conta_saida']['saldo'] = validated_data['conta_saida']['saldo'] - validated_data['valor_transferencia']
            return super().update(instance, validated_data)


