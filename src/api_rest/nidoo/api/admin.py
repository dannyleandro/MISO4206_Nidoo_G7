# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from .models import Oferente, Usuario, Cliente, Ayudante, Parqueadero, Vehiculo, Direccion, Reserva
from django.contrib import admin


# Register your models here.

admin.site.register(Usuario)
admin.site.register(Oferente)
admin.site.register(Cliente)
admin.site.register(Ayudante)
admin.site.register(Parqueadero)
admin.site.register(Vehiculo)
admin.site.register(Direccion)
admin.site.register(Reserva)
