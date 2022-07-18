from rest_framework import serializers
from banco_digital.models.cliente import Cliente


class ClienteSerializer(serializers.HyperlinkedModelSerializer):
    telefone = serializers.CharField(min_length=11)

    class Meta():
        model = Cliente
        fields = "__all__"
