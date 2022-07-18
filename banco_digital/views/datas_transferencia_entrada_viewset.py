from rest_framework import generics
from banco_digital.execptions.conta_inexistente_error import ContaInexistenteError
from banco_digital.models.conta import Conta
from banco_digital.models.transferencia import Transferencia
from banco_digital.serializers.datas_transferencia_entradas_serializer import DatasTransferenciaEntradaSerializer


class DatasTransferenciaEntradaViewSet(generics.ListAPIView):
    """Informa as tranferencias realizadas dentro de um determinado período."""

    def get_queryset(self):
        queryset = Conta.objects.filter(id_conta=self.kwargs['pk'])

        if len(queryset) == 0:
            raise ContaInexistenteError()

        return queryset


    def get_queryset(self):
        queryset = Transferencia.objects.filter(conta_entrada=self.kwargs['pk'],
            data_transferencia__range=(self.kwargs['inicio'], self.kwargs['fim']))

        return queryset

    serializer_class = DatasTransferenciaEntradaSerializer
