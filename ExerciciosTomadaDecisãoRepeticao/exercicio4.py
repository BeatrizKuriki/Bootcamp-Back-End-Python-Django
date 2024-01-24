# Implemente um programa que classifique um aluno com base em sua pontuação em um exame. 
# O programa deverá solicitar uma nota de 0 a 10. 
# Se a pontuação for maior ou igual a 7, o aluno é aprovado; casocontrário, é reprovado.

nota = -1

while nota < 0 or nota > 10:
    nota = int(input('Insira a nota adquirida no exame:'))

if nota >= 7:
    print('Aluno aprovado')
else:
    print('Aluno reprovado')