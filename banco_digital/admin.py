from django.contrib import admin

from banco_digital.models.cliente import Cliente
from banco_digital.models.conta import Conta
from banco_digital.models.transferencia import Transferencia

admin.site.register(Cliente)
admin.site.register(Conta)
admin.site.register(Transferencia)