# -*- coding: utf-8 -*-
from __future__ import unicode_literals

import json
from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
from django.contrib.auth import authenticate, login, logout, update_session_auth_hash
from django.http import HttpResponse, JsonResponse, HttpResponseRedirect, request
# Create your views here.


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


