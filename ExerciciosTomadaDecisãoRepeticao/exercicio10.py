num1 = int(input('Digite um número inteiro: '))
num2 = int(input('Digite um número inteiro: '))
num3 = int(input('Digite um número inteiro: '))

if num1 > num2 and num1 > num3:
    if num2 > num3:
        print(f'1 - {num3} \n2 - {num2} \n3 - {num1}')
    else:
        print(f'1 - {num2} \n2 - {num3} \n3 - {num1}')
elif num2 > num1 and num2 > num3:
    if num1 > num3:
        print(f'1 - {num3} \n2 - {num1} \n3 - {num2}')
    else:
        print(f'1 - {num1} \n2 - {num3} \n3 - {num2}')

else:
    if num1 > num2:
        print(f'1 - {num2} \n2 - {num1} \n3 - {num3}')
    else:
        print(f'1 - {num1} \n2 - {num2} \n3 - {num3}')