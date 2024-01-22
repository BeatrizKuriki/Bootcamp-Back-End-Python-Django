'''Crie um dicionário representando um carrinho de compras.
Adicione produtos (chaves) e quantidades (valores) ao carrinho.
Calcule o total do carrinho de compra. '''

carrinho_compras = {}

carrinho_compras['macas'] = 3
carrinho_compras['uva'] = 4
carrinho_compras['laranja'] = 5
carrinho_compras['banana'] = 1

precos_produto ={'macas': 0.60, 'uva': 3.80, 'laranja':0.74, 'banana':0.75}

total = sum(carrinho_compras[produto] * precos_produto[produto] for produto in carrinho_compras)

print (f'O total do carrinho de compras é R$ {total:.2f}')