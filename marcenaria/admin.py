from django.contrib import admin

from .models import Cliente, Pedido, Produto, Item_Pedido, Materia_Prima, Produto_has_materia_prima, Funcionario, Ordem_Producao 

admin.site.register(Cliente)
admin.site.register(Pedido)
admin.site.register(Produto)
admin.site.register(Item_Pedido)
admin.site.register(Materia_Prima)
admin.site.register(Produto_has_materia_prima)
admin.site.register(Funcionario)
admin.site.register(Ordem_Producao)
