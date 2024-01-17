# Exercícios Conceitos Básicos de Python

# EXERCÍCIO 09

# Solicite ao usuário o número de horas de exercício físico por semana.
# Calcule o total de calorias queimadas em um mês, considerando uma
# média de 5 calorias por minuto de exercício.

# Passos para criação do código

# Solicitar ao usuário o número de horas de exercício físico por semana
# Calcular o total de minutos de exercício em um mês (4 semanas)
# Calcular o total de calorias queimadas em um mês (considerando 5 calorias por minuto)
# Exibir o resultado para o usuário

horasSemana = float(input("Informe a quantidade de horas de exercício praticadas por semana: "))

minutosMes = (horasSemana*60)*4
caloriasMes = minutosMes*5

print("Total de Calorias por mês: ", caloriasMes)