"""
URL configuration for config project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
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
    path('', include(router.urls)),
    path('admin/', admin.site.urls),
]