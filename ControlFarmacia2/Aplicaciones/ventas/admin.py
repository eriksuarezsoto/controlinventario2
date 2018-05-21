from django.contrib import admin

# Register your models here.


from .models import Cajero
from .models import Respaldo_cajero
from .models import Vale1
from .models import Vale2
from .models import Vale3
from .models import Vale4
from .models import Vale5
from .models import Respaldo_Vale
from .models import Respaldo_Vale_total


admin.site.register(Cajero)
admin.site.register(Respaldo_cajero)
admin.site.register(Vale1)
admin.site.register(Vale2)
admin.site.register(Vale3)
admin.site.register(Vale4)
admin.site.register(Vale5)
admin.site.register(Respaldo_Vale_total)
admin.site.register(Respaldo_Vale)
