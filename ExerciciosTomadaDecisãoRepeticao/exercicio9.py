# Exercícios Tomada de Decisão

# EXERCÍCIO 09

# O programa deve calcular e apresentar a quantidade de números pares e
# ímpares inseridos. O processo de leitura deve ser encerrado quando o usuário
# informar o valor zero. Certifique-se de incluir validações para garantir que
# apenas números positivos sejam considerados na contagem e cálculos.


num = int(input("Digite um número positivo: "))
pares = []
impares = []

while num != 0:
    if num < 0:
        print("Esse número é negativo! Tente outro!")
        num = int(input("Digite um número: "))
    elif num % 2 == 0:
        pares.append(num)
        num = int(input("Digite um número: "))
    else :
        impares.append(num)
        num = int(input("Digite um número: "))

print("Quantidade de Números Pares", len(pares))
print("Quantidade de Números Ímpares", len(impares))