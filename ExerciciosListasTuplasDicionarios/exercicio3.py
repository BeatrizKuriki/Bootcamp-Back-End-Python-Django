'''
Crie um dicionário representando um carrinho de compras.
Adicione produtos:chaves e quantidades(valores) ao carrinho.
Calcule o total do carrinho de compra.
'''




carrinho_de_compras = {
    'produto1': 2,
    'produto2': 1,
    'produto3': 3
}


total = sum(carrinho_de_compras.values())

print("Carrinho de Compras:", carrinho_de_compras)
print("Total do Carrinho de Compras:", total)
