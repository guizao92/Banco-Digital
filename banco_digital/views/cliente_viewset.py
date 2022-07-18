from rest_framework import viewsets
from banco_digital.models.cliente import Cliente
from banco_digital.serializers.cliente_serializer import ClienteSerializer


class ClienteViewset(viewsets.ModelViewSet):

    serializer_class = ClienteSerializer
    queryset = Cliente.objects.all()
