# Crie uma função chamada contar_vogais que recebe uma string
# como parâmetro. Implemente a lógica para contar o número de vogais
# na string e retorne o total de vogais. Solicite ao usuário para inserir uma
# frase e utilize a função para contar as vogais.

import re

def conta_vogais(texto):
    padrao = r'[aeiouáéíóúàèìòùãõâêîôûäëïöü]'   
    vogais_encontradas = re.findall(padrao, texto, re.IGNORECASE)
    return len(vogais_encontradas)

frase = input('Digite seu texto aqui:')
print("Total de vogais do texto é de :", conta_vogais(frase))


