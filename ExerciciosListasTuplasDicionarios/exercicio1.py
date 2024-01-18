# Exercícios Tuplas, Listas e Dicionários

# EXERCÍCIO 01

# Utilizando listas faça um programa que faça 5 perguntas para uma
# pessoa sobre um crime.
# As perguntas são:
# ""Telefonou para a vítima?""
# ""Esteve no local do crime?""
# ""Mora perto da vítima?""
# ""Devia para a vítima?""
# ""Já trabalhou com a vítima?""
# O programa deve no final emitir uma classificação sobre a participação
# da pessoa no crime.
# Se a pessoa responder positivamente a 2 questões ela deve ser
# classificada como ""Suspeita"", entre 3 e 4 como ""Cúmplice"" e 5 como
# ""Assassino"".
# Caso contrário,ele será classificado como""Inocente"".

respostas = ["resposta", "resposta", "resposta", "resposta","resposta"]

print('Responda as seguintes perguntas com sim ou não')
respostas[0] = input('Você mora perto da vítima? ').upper()
respostas[1] = input('Já trabalhou com a vítima? ').upper()
respostas[2] = input('Telefonou para a vítima? ').upper()
respostas[3] = input('Esteve no local do crime? ').upper()
respostas[4] = input('Devia para a vítima? ').upper()

soma = respostas.count('SIM')

print(f'Esta pessoa marcou {soma} ponto(s).')

if soma <= 1 :
  print('Esta pessoa está liberada!')
elif soma == 2:
  print('Esta pessoa é uma suspeita')
elif 3 >= soma <= 4 :
  print('Esta pessoa pode ser um cúmplice!')
else:
  print('Esta pessoa pode ser a assassina!')
