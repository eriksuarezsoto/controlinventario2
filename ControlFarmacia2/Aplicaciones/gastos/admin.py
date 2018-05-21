from django.contrib import admin

# Register your models here.


from .models import Gastos2
from .models import Resumen_gastos2
from .models import Cierres2
from .models import Detalle_gastos2
from .models import Cajeros2


admin.site.register(Gastos2)
admin.site.register(Resumen_gastos2)
admin.site.register(Cierres2)
admin.site.register(Detalle_gastos2)
admin.site.register(Cajeros2)
