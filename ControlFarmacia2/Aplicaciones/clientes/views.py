from django.shortcuts import render


def plantilla_cargada(request):
    return render(request, 'inicio.html', {})
