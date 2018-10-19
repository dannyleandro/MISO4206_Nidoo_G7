# -*- coding: utf-8 -*-
from __future__ import unicode_literals

import json
from datetime import datetime

from django.core import serializers
from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
from django.contrib.auth import authenticate, login, logout, update_session_auth_hash
from django.http import HttpResponse, JsonResponse, HttpResponseRedirect, request
# Create your views here.
from .models import Parqueadero, Cliente, Oferente, Vehiculo, Reserva, Usuario, Direccion


def index(request):
    return render(request, 'api/index.html')


@csrf_exempt
def ingresar(request):
    return render(request, "api/login.html")


@csrf_exempt
def login_view(request):
    if request.method == 'POST':
        juser = json.loads(request.body)
        username = juser['username']
        password = juser['password']
        user = authenticate(username=username, password=password)
        if user is not None:
            login(request, user)
            mensaje = "ok"
        else:
            mensaje = "Nombre de usuario o clave no valido"
    return JsonResponse({"mensaje": mensaje})


@csrf_exempt
def logout_view(request):
    logout(request)
    return JsonResponse({"mensaje": 'ok'})


@csrf_exempt
def is_logged_view(request):
    if request.user.is_authenticated:
        mensaje = 'ok'
    else:
        mensaje = 'no'
    return JsonResponse({"mensaje": mensaje})


@csrf_exempt
def get_user_view(request):
    if request.user.is_authenticated:
        return JsonResponse({"username": request.user.username,
                             "first_name": request.user.first_name,
                             "last_name": request.user.last_name,
                             "email": request.user.email})
    else:
        return JsonResponse({"username": ''})


@csrf_exempt
def get_parqueadero(request, parqueadero_id):
    parqueadero = Parqueadero.objects.filter(pk=parqueadero_id)
    if parqueadero is not None:
        return HttpResponse(serializers.serialize("json", parqueadero))
    else:
        return JsonResponse({"nombre": ''})


@csrf_exempt
def reservar_parqueadero(request, parqueadero_id):
    parq = Parqueadero.objects.get(pk=parqueadero_id)
    if parq is not None:
        if request.method == 'POST':
            new_reserva = json.loads(request.body)
            usuario_temp = Usuario.objects.get(pk=new_reserva['cliente'])
            cli = Cliente.objects.get(usuario=usuario_temp)

            fecha = datetime.now()  # new_reserva['fecha']
            veh = Vehiculo.objects.get(vehiculoId=new_reserva['vehiculo'])
            reserva_model = Reserva(Cliente=cli,
                                    Parqueadero=parq,
                                    Fecha=fecha,
                                    Vehiculo=veh)

            reserva_model.save()
            return JsonResponse({"reserva": reserva_model.pk,
                                 "cliente": new_reserva['cliente'],
                                 "parqueadero:": parqueadero_id,
                                 "fecha": fecha,
                                 "vehiculo": new_reserva['vehiculo']})
        else:
            return JsonResponse({"reserva": ''})
    else:
        return JsonResponse({"reserva": 'No existe parqueadero'})


@csrf_exempt
def list_parqueaderos(request):
    return HttpResponse(serializers.serialize("json", Parqueadero.objects.all()))


@csrf_exempt
def list_parqueaderos_disponibles(request):
    disponibles = Parqueadero.objects.filter(reserva=None)
    return HttpResponse(serializers.serialize("json",disponibles))


@csrf_exempt
def list_reservas(request):
    return HttpResponse(serializers.serialize("json", Reserva.objects.all()))


@csrf_exempt
def add_parqueadero(request):
    if request.method == 'POST':
        new_parqueadero = json.loads(request.body)
        print(new_parqueadero)
        usuario_temp = Usuario.objects.get(pk=new_parqueadero['oferente'])
        ofe = Oferente.objects.get(usuario=usuario_temp)
        dir = Direccion.objects.get(pk=new_parqueadero['direccion'])
        parqueadero_model = Parqueadero(oferente=ofe,
                                        direccion=dir,
                                        tipoVehiculo=new_parqueadero['tipoVehiculo'],
                                        tipoDisponibilidad=new_parqueadero['tipoDisponibilidad'],
                                        caracteristicas=new_parqueadero['caracteristicas'],
                                        longitud=new_parqueadero['longitud'],
                                        latitud=new_parqueadero['latitud'])

        parqueadero_model.save()
        return JsonResponse({"parqueadero": parqueadero_model.pk,
                             "oferente": new_parqueadero['oferente'],
                             "direccion": new_parqueadero['direccion'],
                             "tipoVehiculo": parqueadero_model.tipoVehiculo,
                             "tipoDisponibilidad": parqueadero_model.tipoDisponibilidad,
                             "caracteristicas": new_parqueadero['caracteristicas'],
                             "longitud": new_parqueadero['longitud'],
                             "latitud": new_parqueadero['latitud']})
    else:
        return JsonResponse({"parqueadero": ''})
