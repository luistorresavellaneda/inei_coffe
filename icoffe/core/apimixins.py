from rest_framework import status
from rest_framework.response import Response
import random


class CreaMultiMixin(object):
    def create(self, request, *args, **kwargs):
        datos = request.data
        for data in datos:
            serializer = self.get_serializer(data=data)
            if serializer.is_valid(raise_exception=False):
                self.perform_create(serializer)

        return Response({"success": True}, status=status.HTTP_201_CREATED)

def CodigoAleaotrioMixin(longitud, contenido, lista):
    aleatorio = ''.join(random.choice(contenido) for _ in range(longitud))

    while aleatorio in lista:
        aleatorio = ''.join(random.choice(contenido) for _ in range(longitud))

    return aleatorio
