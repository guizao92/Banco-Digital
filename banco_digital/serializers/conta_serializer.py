from rest_framework import serializers
from banco_digital.models.conta import Conta


class ContaSerializer(serializers.HyperlinkedModelSerializer):
    saldo = serializers.FloatField(required=False)

    class Meta():
        model = Conta
        fields = "__all__"

    def validated_data(self):
        return super().validated_data

    def update(self, instance, validated_data):
        validated_data['saldo'] = validated_data['saldo'] - 10
        return super().update(instance, validated_data)
