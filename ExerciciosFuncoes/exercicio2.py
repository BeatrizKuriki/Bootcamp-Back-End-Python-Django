# Reverso do número.Faça uma função que retorne o reverso de um úmero inteiro informado.Por exemplo:127->721

def reverse(num):
    result = ''.join(reversed(str(num)))
    return int(result)  


numInt = input('Informe um número inteiro:')
print(reverse(int(numInt)))
