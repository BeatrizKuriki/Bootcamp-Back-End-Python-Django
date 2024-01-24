'''
Faça um programa que peça 2 números e imprima o maior deles
'''
num1 = int(input("Digite o numero 1: "))
num2 = int(input("Digite o numero 2: "))

if num1 > num2:
    print(f"O maior número é: {num1}")
elif num2 > num1:
    print(f"O maior número é: {num2}")
else:
    print("Os números são iguais.")
