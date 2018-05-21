
from django.conf.urls import path
from . import views


urlpatterns = [
    path('', views.Holita, name='Holita'),
    path('', views.lista_de_productos, name='lista_de_productos')
]
