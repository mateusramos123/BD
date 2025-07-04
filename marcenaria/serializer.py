from rest_framework.serializers import ModelSerializer

from .models import Cliente, Pedido, Produto, Item_Pedido, Materia_Prima, Produto_has_materia_prima, Funcionario, Ordem_Producao

class ClienteSerializer(ModelSerializer):
    class Meta:
        model = Cliente
        fields = '__all__'

class PedidoSerializer(ModelSerializer):
    class Meta:
        model = Pedido
        fields = '__all__'

class ProdutoSerializer(ModelSerializer):
    class Meta:
        model = Produto
        fields = '__all__'

class ItemPedidoSerializer(ModelSerializer):
    class Meta:
        model = Item_Pedido
        fields = '__all__'

class MateriaPrimaSerializer(ModelSerializer):
    class Meta:
        model = Materia_Prima
        fields = '__all__'

class ProdutoHasMateriaPrimaSerializer(ModelSerializer):
    class Meta:
        model = Produto_has_materia_prima
        fields = '__all__'

class FuncionarioSerializer(ModelSerializer):
    class Meta:
        model = Funcionario
        fields = '__all__'

class OrdemProducaoSerializer(ModelSerializer):
    class Meta:
        model = Ordem_Producao
        fields = '__all__'
