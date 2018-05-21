from django.contrib import admin

# Register your models here.


from .models import Clientes2
from .models import Registro_ventas2
from .models import Contactos


admin.site.register(Clientes2)
admin.site.register(Registro_ventas2)
admin.site.register(Contactos)
