from rest_framework import serializers
from ..models import Reserva, Mesa


class MesaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Mesa
        fields = ('codigo',)

class ReservaSerializer(serializers.ModelSerializer):
    #mesa = MesaSerializer()
    class Meta:
        model = Reserva
        fields = ('nombres', 'apellidos', 'dni', 'nro_personas', 'fecha', 'detalle', 'mesa')