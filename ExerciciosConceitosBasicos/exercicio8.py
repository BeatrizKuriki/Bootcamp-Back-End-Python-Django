# Faça um Programa que pergunte quanto você ganha por hora e o
# número de horas trabalhadas no mês.Calcule e mostre o total do seu
# salário no referido mês

valor = float(input('Quanto você ganha por hora??'))
hora = float(input('Quantas horas você trabalha por mês?'))

salario = valor * hora
print(f'O seu salário mensal será de R$ {salario} reais')