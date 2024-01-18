# EXERCICIO 4
# Receba do usuário a quantidade de litros de combustível consumidos e a distância percorrida.
# Calcule e imprima o consumo médio em km/l.

litrosConsumidos = float(input('Digite a quantidade de litros de combustível que foi consumida:'))
distanciaPercorrida = float(input('Digite qual foi a distância percorrida:'))
consumoMedio = distanciaPercorrida/litrosConsumidos
print(f'O consumo médio do veículo foi de {consumoMedio:.1f} km/l')