from django.contrib import admin
from django.urls import include, path
from rest_framework import routers
from banco_digital.views.cliente_viewset import ClienteViewset
from banco_digital.views.consulta_saldo_conta_viewset import ConsultaSaldoContaViewSet
from banco_digital.views.conta_viewset import ContaViewSet
from banco_digital.views.datas_transferencia_entrada_viewset import DatasTransferenciaEntradaViewSet
from banco_digital.views.datas_transferencia_saidas_viewset import DatasTransferenciaSaidasViewSet
from banco_digital.views.lista_contas_cliente_viewset import ListaContasClienteViewSet
from banco_digital.views.transferencia_viewset import TransferenciaViewSet

router = routers.DefaultRouter()
router.register(r'cliente', ClienteViewset)
router.register(r'conta', ContaViewSet)
router.register(r'transferencia', TransferenciaViewSet)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include(router.urls)),
    path('cliente/<int:pk>/contas/', ListaContasClienteViewSet.as_view()),
    path('conta/<int:pk>/saldo', ConsultaSaldoContaViewSet.as_view()),
    path('conta/<int:pk>/entradas/<inicio>/<fim>', DatasTransferenciaEntradaViewSet.as_view()),
    path('conta/<int:pk>/saidas/<inicio>/<fim>', DatasTransferenciaSaidasViewSet.as_view()),     
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework'))
]
