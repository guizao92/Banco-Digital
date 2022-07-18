from rest_framework import serializers
from banco_digital.execptions.conta_inexistente_error import ContaInexistenteError
from banco_digital.models.transferencia import Transferencia


class DatasTransferenciaSaidasSerializer(serializers.ModelSerializer):
    transferencia = serializers.ReadOnlyField(
        source='transferencia.id_transferencia')

    class Meta:
        model = Transferencia
        fields = ['transferencia', 'id_transferencia',
                  'data_transferencia', 'valor_transferencia', 'conta_entrada']
