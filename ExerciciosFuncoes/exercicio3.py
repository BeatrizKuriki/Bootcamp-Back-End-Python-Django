# Escreva um script que pergunta ao usuário se ele deseja converter uma temperatura de grau Celsius para Fahrenheit ou vice-versa.Para cada opção,crie uma função.



def convert_celsius_fahrenheit(celsius):
    return (celsius *9/5) + 32


def convert_fahrenheit_celsius(fahrenheit):
    return (fahrenheit -32) * 5/9

print("Escolha o tipo de conversão que você deseja:")
print("1: Celsius para Fahrenheit")
print("2: Fahrenheit para Celsius")
escolha = input("Digite 1 ou 2: ")


if escolha == '1':
    celsius = float(input("Informe a temperatura em Celsius: "))
    print(f"{celsius} graus Celsius é igual a {convert_celsius_fahrenheit(celsius)} graus Fahrenheit.")

elif escolha == '2':
    fahrenheit = float(input("Informe a temperatura em Fahrenheit: "))
    print(f"{fahrenheit} graus Fahrenheit é igual a {convert_fahrenheit_celsius(fahrenheit)} graus Celsius.")
else:
    print('Opção inválida, por favor escolha 1 ou 2')    


