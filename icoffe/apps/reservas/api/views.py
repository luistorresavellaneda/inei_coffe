from core.apimixins import CodigoAleaotrioMixin
from rest_framework.generics import (
    ListAPIView,
    CreateAPIView,
    UpdateAPIView,
    DestroyAPIView
)
from .serializers import ReservaSerializer
from ..models import Reserva, Mesa
import string


class ReservaApiView(ListAPIView, CreateAPIView):
    serializer_class = ReservaSerializer
    queryset = Reserva.objects.all()

    def perform_create(self, serializer):
        data = serializer.data
        reserva = Reserva()
        codigos = Reserva.objects.values_list('codigo', flat=True)
        reserva.codigo = CodigoAleaotrioMixin(10,string.ascii_uppercase+string.digits,list(codigos))
        reserva.nombres = data['nombres']
        reserva.apellidos = data['apellidos']
        reserva.dni = data['dni']
        reserva.nro_personas = data['nro_personas']
        reserva.fecha = data['fecha']
        reserva.detalle = data['detalle']
        reserva.mesa_id = data['mesa']

        reserva.save()