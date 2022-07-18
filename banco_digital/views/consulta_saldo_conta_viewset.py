from rest_framework import generics
from banco_digital.execptions.conta_inexistente_error import ContaInexistenteError
from banco_digital.models.conta import Conta
from banco_digital.serializers.consulta_saldo_conta_serializer import ConsultaSaldoContaSerializer


class ConsultaSaldoContaViewSet(generics.ListAPIView):
    """Consultando saldo de uma conta específica"""

    def get_queryset(self):
        queryset = Conta.objects.filter(id_conta=self.kwargs['pk'])
        
        if len(queryset) == 0:
            raise ContaInexistenteError()

        return queryset


    serializer_class = ConsultaSaldoContaSerializer
