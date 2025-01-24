from django.contrib import admin
from .models import Usuario, Carteira, Transferencia

admin.site.register(Usuario)
admin.site.register(Carteira)
admin.site.register(Transferencia)