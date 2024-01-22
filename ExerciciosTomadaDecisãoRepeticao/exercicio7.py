'''Desenvolver um programa que solicite a idade do usuário e identifique 
se ele é uma criança, uma dolescente, adulto ou idoso.
                Criança 0 a 12 anos.
                Adolescente 13 a 17 anos.
                Adulto 18 a 59 anos.
                Idoso 60 anos ou mais.
'''
idade = int(input('Digite a sua idade: '))
if idade <= 12:
  print('Criança')

elif idade <= 17:
  print('Adolescente')

elif idade <= 59:
  print('Adulto')

elif idade >= 60:
  print('Idoso')

