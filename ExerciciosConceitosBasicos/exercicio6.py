''' Escreva um programa que calcule o tempo de uma viagem.
Faça um comparativo do mesmo percurso de avião, carro e ônibus.
Levando em consideração:
avião=600km/h
carro=100km/h
ônibus=80km/h    '''


print('Olá!')
km = float(input('Quantos km tem sua viagem? '))
aviao = km / 600
carro = km / 100
onibus = km / 80

print('Analisando a quilometragem da sua viagem no valor de {}km, de avião levaria {}h, de carro {}h e de ônibus {}h ' .format(km, aviao, carro, onibus))