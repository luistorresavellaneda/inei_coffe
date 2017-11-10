from django.conf.urls import url
from .views import ReservaApiView

urlpatterns = [
    url(r'^$', ReservaApiView.as_view(), name='lista_reserva'),
]