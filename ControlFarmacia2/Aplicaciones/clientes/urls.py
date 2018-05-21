from django.urls import path
from . import views


urlpatterns = [
    path('templateclientes/', views.contacto, name='contacto')
]