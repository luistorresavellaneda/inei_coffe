from django.contrib import admin
from .models import Reserva
# Register your models here.

@admin.register(Reserva)
class ReservaAdmin(admin.ModelAdmin):
    pass
