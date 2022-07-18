from rest_framework import viewsets, generics, filters
from banco_digital.models.transferencia import Transferencia
from banco_digital.serializers.transferencia_serializer import TransferenciaSerializer
from django_filters.rest_framework import DjangoFilterBackend

class TransferenciaViewSet(viewsets.ModelViewSet):

    # def AtualizaSaldos(self):
    #     conta_entrada = Transferencia.objects.get(self, 'conta_entrada')
    #     conta_saida = Transferencia.objects.get(self, 'conta_saida')
    #     valor_transferencia = Transferencia.objects.get(self, 'valor_transferencia')

    #     conta_entrada.saldo = conta_entrada.saldo + valor_transferencia
    #     conta_entrada.save()
    #     conta_saida.saldo = conta_saida.saldo - valor_transferencia
    #     conta_saida.save()

    #     return None    
    
    serializer_class = TransferenciaSerializer
    queryset = Transferencia.objects.all()
   

    # filter_backends = [
    #     DjangoFilterBackend,
    #     filters.OrderingFilter,
    #     filters.SearchFilter
    # ]
    # filter_setfields = {'data_transferencia': ['exact', 'gte', 'lte']}
    # search_fields = ['data_transferencia']
    # ordering_fields = ['data_transferencia']

