from django.contrib import admin

# Register your models here.


from .models import Factura
from .models import Detalle_facturas
from .models import Ingreso_facturas1
from .models import Ingreso_facturas2
from .models import Ingreso_facturas3
from .models import Ingreso_facturas4
from .models import Ingreso_facturas5
from .models import Proveedor


admin.site.register(Factura)
admin.site.register(Detalle_facturas)
admin.site.register(Ingreso_facturas1)
admin.site.register(Ingreso_facturas2)
admin.site.register(Ingreso_facturas3)
admin.site.register(Ingreso_facturas4)
admin.site.register(Ingreso_facturas5)
admin.site.register(Proveedor)
