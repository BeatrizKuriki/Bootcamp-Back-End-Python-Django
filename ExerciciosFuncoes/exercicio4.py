# Crie um programa que leia quanto dinheiro uma pessoa tem na carteira, e calcule quanto poderia comprar de cada moeda estrangeira. 
# Considere a tabela de conversão abaixo: 
# Dólar Americano: R$4,91 
# Peso Argentino: R$0,02 
# Dólar Australiano: R$3,18
# Dólar Canadense: R$3,64
# Franco Suiço: R$0,42
# Euro: R$5,36
# Libraesterlina: R$6,21

carteira = float(input('Quantos reais você tem na carteira? '))

def conversor_de_moeda(carteira):
    dolar_americano = carteira / 4.91
    peso_argentino = carteira / 0.02
    dolar_australiano = carteira / 3.18
    dolar_canadense = carteira / 3.64
    franco_suico = carteira / 0.42
    euro = carteira / 5.36
    libraesterlina = carteira / 6.21
    
    print(f'Com o valor disponível na sua carteira, você poderia comprar {dolar_americano:.2f} dolares americanos, ou {peso_argentino:.2f} pesos argentinos, ou {dolar_australiano:.2f} dolares australianos, ou {dolar_canadense:.2f} dolares canadenses, ou {franco_suico:.2f} francos suiços, ou {euro:.2f} euros, ou {libraesterlina:.2f} libraesterlinas');

conversor_de_moeda(carteira)