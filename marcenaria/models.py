from django.db import models

class Cliente (models.Model):
    nome_cliente = models.CharField(max_length=45)
    email_cliente = models.EmailField(max_length=45, unique=True)
    cpf_cliente = models.CharField(max_length=11, unique=True)
    endereco_cliente = models.CharField(max_length=200)
    telefone_cliente = models.CharField(max_length=45)

    def __str__(self):
        return f'{self.nome_cliente} (CPF: {self.cpf_cliente})'


class Pedido (models.Model):
    data_pedido = models.DateField()
    valor_pedido = models.DecimalField(max_digits=10, decimal_places=2)
    status_pedido = models.CharField(max_length=20)
    forma_pag_pedido = models.CharField(max_length=45)
    cliente = models.ForeignKey(Cliente, on_delete=models.PROTECT)

    def __str__(self):
       return f'Pedido: {self.cliente} - {self.data_pedido}'

class Produto (models.Model):
    nome_produto = models.CharField(max_length=45)
    descricao_produto = models.CharField(max_length=150)
    valor_produto = models.DecimalField(max_digits=10, decimal_places=2)
    estoque_produto = models.IntegerField()
    
    def __str__(self):
       return f'Produto: {self.nome_produto} - (R$ {self.valor_produto})'
    
    
class Item_Pedido (models.Model):
    pedido = models.ForeignKey(Pedido, on_delete=models.PROTECT)
    produto = models.ForeignKey(Produto, on_delete=models.PROTECT)
    quantidade_item_pedido = models.IntegerField() 

    def __str__(self):
        return f'Item Pedido: {self.pedido}, Produto: {self.produto} - Quantidade: {self.quantidade_item_pedido}'
     

class Materia_Prima(models.Model):
    nome_materia = models.CharField(max_length=45)
    descricao_materia = models.CharField(max_length=150)
    estoque_materia = models.IntegerField()

    def __str__(self):
        return f'Matéria: {self.nome_materia} - Estoque: {self.estoque_materia}'
 
class Produto_has_materia_prima (models.Model):
    produto = models.ForeignKey(Produto, on_delete=models.PROTECT)
    materia_prima = models.ForeignKey(Materia_Prima, on_delete=models.PROTECT)

    def __str__(self):
         return f'{self.produto} usa {self.materia_prima}'

class Funcionario (models.Model):
    nome_funcionario = models.CharField(max_length=45)
    cpf_funcionario = models.CharField(max_length=11, unique= True)
    email_funcionario = models.EmailField(max_length=45, unique= True)

    def __str__(self):
        return f' {self.nome_funcionario} - {self.email_funcionario}'
    
class Ordem_Producao (models.Model):
    funcionario = models.ForeignKey(Funcionario, on_delete=models.PROTECT)    
    materia_prima = models.ForeignKey(Materia_Prima, on_delete=models.PROTECT)
    produto = models.ForeignKey(Produto, on_delete=models.PROTECT)
    quantidade_produto = models.IntegerField()
    
    def __str__(self):
        return f'Produto: {self.produto} - Quantidade: {self.quantidade_produto}'