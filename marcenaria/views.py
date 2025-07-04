from rest_framework.viewsets import ModelViewSet
from .models import Cliente, Pedido, Produto, Item_Pedido, Materia_Prima, Produto_has_materia_prima, Funcionario, Ordem_Producao
from .serializer import ClienteSerializer, PedidoSerializer, ProdutoSerializer, ItemPedidoSerializer, MateriaPrimaSerializer, ProdutoHasMateriaPrimaSerializer, FuncionarioSerializer, OrdemProducaoSerializer

class ClienteViewSet(ModelViewSet):
    queryset = Cliente.objects.all()
    serializer_class = ClienteSerializer

class PedidoViewSet(ModelViewSet):
    queryset = Pedido.objects.all()
    serializer_class = PedidoSerializer

class ProdutoViewSet(ModelViewSet):
    queryset = Produto.objects.all()
    serializer_class = ProdutoSerializer

class ItemPedidoViewSet(ModelViewSet):
    queryset = Item_Pedido.objects.all()
    serializer_class = ItemPedidoSerializer

class MateriaPrimaViewSet(ModelViewSet):
    queryset = Materia_Prima.objects.all()
    serializer_class = MateriaPrimaSerializer

class ProdutoHasMateriaPrimaViewSet(ModelViewSet):
    queryset = Produto_has_materia_prima.objects.all()
    serializer_class = ProdutoHasMateriaPrimaSerializer

class FuncionarioViewSet(ModelViewSet):
    queryset = Funcionario.objects.all()
    serializer_class = FuncionarioSerializer

class OrdemProducaoViewSet(ModelViewSet):
    queryset = Ordem_Producao.objects.all()
    serializer_class = OrdemProducaoSerializer
