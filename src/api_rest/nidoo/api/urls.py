from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.index, name='index'),
    # url(r'^ingresar/$', views.ingresar, name='ingresar'),
    # url(r'^login/$', views.login_view, name='login'),
    # url(r'^logout/$', views.logout_view, name='logout'),
    # url(r'^isLogged/$', views.is_logged_view, name='isLogged'),
    # url(r'^getUser/$', views.get_user_view, name='getUser'),
    # url(r'^usuario/(?P<userId>\d+)$', views.get_user_view, name='getUser'),
    url(r'^parqueadero/(?P<parqueadero_id>\d+)$', views.get_parqueadero, name='parqueadero'),
    url(r'^parqueadero/(?P<parqueadero_id>\d+)/reservar$', views.reservar_parqueadero, name='reservar_parqueadero'),
    url(r'^parqueaderos/$', views.list_parqueaderos, name='parqueaderos'),
    url(r'^parqueaderosDisponibles/$', views.list_parqueaderos_disponibles, name='parqueaderos_disp'),
    url(r'^parqueaderosDisponibles/(?P<pagina_id>\d+)$', views.list_parqueaderos_disponibles_pagina, name='parqueaderos_disp'),
    url(r'^parqueadero/', views.add_parqueadero, name='agregar_parqueadero'),
    url(r'^reservas/$', views.list_reservas, name='reservas'),

]
