from django.contrib import admin

# Register your models here.


from .models import Ventas_mensuales2
from .models import Resumen_vendedores2
from .models import Datos_local2
from .models import Ultima_boleta2
from .models import Password2
from .models import Observaciones2


admin.site.register(Ventas_mensuales2)
admin.site.register(Resumen_vendedores2)
admin.site.register(Datos_local2)
admin.site.register(Ultima_boleta2)
admin.site.register(Password2)
admin.site.register(Observaciones2)
