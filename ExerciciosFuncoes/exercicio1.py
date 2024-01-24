'''
Faça um programa que  necessite de três argumentos, e que forneça a soma desses três argumentos.
'''

def soma(a, b, c):
    resultado = a + b + c
    return resultado

num1 = 5
num2 = 7
num3 = 3

resultado_soma = soma(num1, num2, num3)

print(f'O resultado da soma é: {resultado_soma}')
