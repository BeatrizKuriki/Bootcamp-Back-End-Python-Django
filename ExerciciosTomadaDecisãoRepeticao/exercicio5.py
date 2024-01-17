#Desenvolva um programa que solicite ao usuário os comprimentos dos três
# lados de um triângulo e classifique-o como equilátero, isósceles ou escaleno.
# equilátero: todos os lados com o mesmo valor
# isósceles: dois lados com o mesmo valor
# escaleno: todos os lados com medidas distintas.

#EXERCÍCIO 5

ladoA = int(input('Informe o primeiro lado do triângulo:'))
ladoB = int(input('Informe o segundo lado do triângulo:'))
ladoC = int(input('Informe o terceiro lado do triângulo:'))


if (ladoA + ladoB) < ladoC or (ladoA + ladoC) < ladoB or (ladoB + ladoC) < ladoA:
    print("Não é um triângulo")
elif (ladoA == ladoB) and (ladoA == ladoC) and (ladoB == ladoC):
    print('É um triângulo equilátero!!') 
elif (ladoA==ladoB) or (ladoA==ladoC) or (ladoB==ladoC):
        print('É um triângulo isósceles')   
else:
     print('É um triângulo escaleno')         

