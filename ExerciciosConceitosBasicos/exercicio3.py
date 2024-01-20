# Solicitar a quantidade de quilômetros ao usuário
quilometros = float(input("Digite a quantidade de quilômetros: "))

# Realizar as conversões
metros = quilometros * 1000
centimetros = metros * 100
milimetros = centimetros * 10

# Exibir os resultados
print(f"{quilometros} quilômetros é igual a:")
print(f"{metros} metros")
print(f"{centimetros} centímetros")
print(f"{milimetros} milímetros")
