from django.contrib import admin
from django.urls import path, include

from rest_framework.routers import DefaultRouter
from marcenaria.views import ClienteViewSet, PedidoViewSet, ProdutoViewSet, ItemPedidoViewSet, MateriaPrimaViewSet, ProdutoHasMateriaPrimaViewSet, FuncionarioViewSet, OrdemProducaoViewSet

router = DefaultRouter()
router.register(r'Clientes', ClienteViewSet)
router.register(r'Pedidos', PedidoViewSet)
router.register(r'Produtos', ProdutoViewSet)
router.register(r'Itens_Pedidos', ItemPedidoViewSet)
router.register(r'Materias_Primas', MateriaPrimaViewSet)
router.register(r'Produtos_Has_Materias_Primas', ProdutoHasMateriaPrimaViewSet)
router.register(r'Funcionarios', FuncionarioViewSet)
router.register(r'Ordem_Producoes', OrdemProducaoViewSet)

urlpatterns = [
    path('api/', include(router.urls)),
    path('admin/', admin.site.urls),
]