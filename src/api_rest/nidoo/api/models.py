# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.db import models
from django.contrib.auth.models import AbstractUser
# Create your models here.


class User(AbstractUser):
    is_cliente = models.BooleanField(default=False)
    is_oferente = models.BooleanField(default=False)
    identificacion = models.CharField(max_length=20)
    celular = models.CharField(max_length=20)


class Oferente(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, primary_key=True)


class Cliente(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, primary_key=True)


class Ayudante(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, primary_key=True)


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
    complemento = models.CharField(max_length=255)


class Parqueadero(models.Model):
    direccion = models.ForeignKey(Direccion, on_delete=models.CASCADE)
    tipoVehiculo = models.CharField(max_length=20, choices=VEHICLE_TYPE, default='C')
    tipoDisponibilidad = models.CharField(max_length=10, choices=TIME_TYPE, default='A')
    caracteristicas = models.CharField(max_length=255)
    oferente = models.ForeignKey(Oferente, on_delete=models.CASCADE)


class Vehiculo(models.Model):
    cliente = models.ForeignKey(Oferente, on_delete=models.CASCADE)
    tipo = models.CharField(max_length=20, choices=VEHICLE_TYPE, default='C')
    placa = models.CharField(max_length=10),
    marca = models.CharField(max_length=255),
    modelo = models.CharField(max_length=255)
    es_principal = models.BooleanField(default=False)
