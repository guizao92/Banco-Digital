from rest_framework import serializers, generics
from banco_digital.execptions.conta_inexistente_error import ContaInexistenteError
from banco_digital.models.conta import Conta
from banco_digital.models.transferencia import Transferencia
from banco_digital.serializers.conta_serializer import ContaSerializer   
    
class AtualizaSaldosViewSet(generics.UpdateAPIView):

    serializer_class = ContaSerializer

    def get_queryset(self):
        queryset = Conta.objects.filter(id_conta=self.kwargs['pk'])
        
        if len(queryset) == 0:
            raise ContaInexistenteError()

        return queryset

    def patch(self, request, *args, **kwargs):
        return self.update(request, *args, **kwargs)

