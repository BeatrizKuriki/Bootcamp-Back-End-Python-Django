#EXERCICIO1

#EXERCICIO2     


#EXERCICIO3


#EXERCICIO4     


#EXERCICIO5 
'''
Escreva um programa que calcule o salário líquido.Lembrando de declarar o salário bruto e o percentual de desconto do Imposto de Renda.
●Renda até R$1.903,98:isento de imposto de renda;
●Renda entre R$1.903,99 e R$2.826,65:alíquota de 7,5%;
●Renda entre R$2.826,66 e R$3.751,05:alíquota de 15%;
●Renda entre R$3.751,06 e R$4.664,68:alíquota de 22,5%; 
●Renda acima de R$4.664,68:alíquota máxima de 27,5%
'''
salario = input('Informe seu salário, por favor:')
salario = float(salario)

if salario <= 1903.98:
    print('Parabéns, você está isento de cobrança de imposto de renda')
elif salario >= 1903.99 and salario <= 2806.65:
    salarioDesconto  = salario -(salario *7.5)/100
    print(f'O valor informado foi de R${salario} reais. O seu percentual de desconto do é de 7.5% e o valor do seu salário será de R$ {salarioDesconto}')

elif salario >= 2826.66  and salario <= 3751.05:
    salarioDesconto  = salario -(salario *15)/100
    print(f'O valor informado foi de R${salario}reais . O seu percentual de desconto do é de 15% e o valor do seu salário será de R$ {salarioDesconto}')

elif salario >= 3751.06  and salario <= 4664.68:
    salarioDesconto  = salario-(salario *22.5)/100
    print(f'O valor informado foi de R${salario} reais. O seu percentual de desconto do é de 22.5% e o valor do seu salário será de R$ {salarioDesconto}')    
elif salario > 4664.68:
    salarioDesconto  = salario-(salario *27.5)/100
    print(f'O valor informado foi de R${salario} reais. O seu percentual de desconto do é de 27.5% e o valor do seu salário será de R$ {salarioDesconto} reais') 

    


#EXERCICIO6 

#EXERCICIO7

#EXERCICIO8

#EXERCICIO9

#EXERCICIO10