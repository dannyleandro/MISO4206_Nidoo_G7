# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.db import models
from django.contrib.auth.models import AbstractUser
# Create your models here.


class Usuario(AbstractUser):
    is_cliente = models.BooleanField(default=False)
    is_oferente = models.BooleanField(default=False)
    identificacion = models.CharField(max_length=20)
    celular = models.CharField(max_length=20)

    def __str__(self):
        return self.username


class Oferente(models.Model):
    usuario = models.OneToOneField(Usuario, on_delete=models.CASCADE, primary_key=True)


class Cliente(models.Model):
    usuario = models.OneToOneField(Usuario, on_delete=models.CASCADE, primary_key=True)


class Ayudante(models.Model):
    user = models.OneToOneField(Usuario, on_delete=models.CASCADE, primary_key=True)


VEHICLE_TYPE = (
    ('M', 'Motocicleta'),
    ('B', 'Bicicleta'),
    ('C', 'Carro')
)

TIME_TYPE = (
    ('A', '24/7'),
    ('B', 'L/V 24Hrs'),
    ('C', 'L/V 7am-9pm'),
    ('D', 'Otro horario')
)


class Direccion(models.Model):
    nombre_direccion = models.CharField(max_length=255)
    complemento = models.CharField(max_length=255, null=True)


class Parqueadero(models.Model):
    ParqueaderoId = models.AutoField(primary_key=True)
    oferente = models.ForeignKey(Oferente)
    direccion = models.ForeignKey(Direccion)
    tipoVehiculo = models.CharField(max_length=20, choices=VEHICLE_TYPE, default='C')
    tipoDisponibilidad = models.CharField(max_length=10, choices=TIME_TYPE, default='A')
    caracteristicas = models.CharField(max_length=255)


class Vehiculo(models.Model):
    vehiculoId = models.AutoField(primary_key=True)
    cliente = models.ForeignKey(Cliente)
    tipo = models.CharField(max_length=20, choices=VEHICLE_TYPE, default='C')
    placa = models.CharField(max_length=10, null=True)
    marca = models.CharField(max_length=255, null=True)
    modelo = models.CharField(max_length=255, null=True)
    es_principal = models.BooleanField(default=False)


class Reserva(models.Model):
    Cliente = models.ForeignKey(Cliente)
    Parqueadero = models.ForeignKey(Parqueadero)
    Fecha = models.DateTimeField()
    Vehiculo = models.ForeignKey(Vehiculo)
