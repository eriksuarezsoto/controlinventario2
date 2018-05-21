from django.http import HttpResponse
from django.shortcuts import render
# , redirect, get_object_or_404


def Holita(request):
    return HttpResponse('holaaaaaaaa')


# def lista_de_productos(request):
  #  produc = Listado_productos.objects.all.order_by('codigo')
   # context = {'produc': produc}

    # return render(request, 'produc/list.html', context)
