from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^ingresar/$', views.ingresar, name='ingresar'),
    url(r'^login/$', views.login_view, name='login'),
    # url(r'^logout/$', views.logout_view, name='logout'),
    # url(r'^isLogged/$', views.is_logged_view, name='isLogged'),
    # url(r'^usuario/(?P<userId>\d+)$', views.get_user_view, name='getUser'),
    # url(r'^parqueadero/(?P<parqueaderoId>\d+)$', views.get_parqueadero, name='parqueadero'),
    # url(r'^parqueadero/(?P<parqueaderoId>\d+)/reservar$', views.reservar_parqueadero, name='reservar_parqueadero'),
    # url(r'^reservar/$', views.get_user_view, name='getUser'),
]
