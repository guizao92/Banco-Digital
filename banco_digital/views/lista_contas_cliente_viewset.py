from rest_framework import generics
from banco_digital.models.conta import Conta
from banco_digital.serializers.lista_contas_cliente_serializer import ListaContasClienteSerializer


class ListaContasClienteViewSet(generics.ListAPIView):
    """Listando todas as contas de um cliente"""

    def get_queryset(self):
        queryset = Conta.objects.filter(cliente_id=self.kwargs['pk'])
        return queryset

    serializer_class = ListaContasClienteSerializer