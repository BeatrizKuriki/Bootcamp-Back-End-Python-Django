import random
from os import system, name
import unidecode
import csv

#Função para limpar tela em windows ou mac/linux
def limpa_tela():
    if name == 'nt':
        _ = system('cls')
    else :
        _ = system('clear')

#Função para garantir que letras acentuadas não serão diferenciadas
def to_ascii(ls):
    for i in range(len(ls)):
        ls[i] = unidecode.unidecode(ls[i])

#Introdução ao jogo
def game():

    limpa_tela()
    print('\nBoas vindas ao Jogo da Forca!')
    print('Escolha um tema:\n')
    print('1 - Animais\n')
    print('2 - Capitais\n')
    print('3 - Esportes\n')
    print('4 - Frutas\n')

    #Definir a lista de palavras possíveis a partir de arquivo csv
    with open('palavrascsv.csv', 'r', encoding='utf8', newline = '\r\n') as arquivo:
        
        # Cria o objeto de leitura
        leitor = csv.reader(arquivo)
        # Cria lista de listas
        palavras = list(leitor)
        # Cria novas listas para cada tema
        frutas = [sublista[0] for sublista in palavras[1:]]
        esportes = [sublista[1] for sublista in palavras[1:]]
        animais = [sublista[2] for sublista in palavras[1:]]
        capitais = [sublista[3] for sublista in palavras[1:]]
        

    #Escolher uma palavra aleatória da lista
    while True:
        alternativa = input('Escolha seu tema (1/2/3/4): ')
        if alternativa.isdigit():
            alternativa = int(alternativa)      
            if alternativa == 1:
                palavra = random.choice(animais).upper()
                break
            elif alternativa == 2:
                palavra = random.choice(capitais).upper()
                break
            elif alternativa == 3:
                palavra = random.choice(esportes).upper()
                break
            elif alternativa == 4:
                palavra = random.choice(frutas).upper()
                break
            else: 
                print('Por favor, digite somente um número dentre as opções!\n')
        else:
            print('Por favor, digite somente um número dentre as opções!\n')  
    
    #Criando lista vazia para caracteres já utilizados    
    letras_utilizadas = []

    chances = 5

    #Usando list comprehension para exibir palavra secreta
    palavra_secreta = ['_' for letra in palavra]

    while chances > 0:
        print('\n',' '.join(palavra_secreta))
        print('\nLetras Utilizadas: ', ' '.join(letras_utilizadas))
        print(f'Chances Restantes: {chances}')

        #Pedindo digitação de letra e verificação de que somente um caractere é digitado
        while True:
            letra_adivinhada = input('\nDigite uma letra: ').upper()
            caracteres_em_chute = len(letra_adivinhada)
            if caracteres_em_chute > 1:
                print('Por favor, digite somente uma letra!')
            else:
                break
        
        #Verificando se letra está em palavra secreta
        if letra_adivinhada in palavra:
            i = 0
            #Percorra cada letra da palavra a partir do indíce e verifique se a letra pode ser substituída pela letra digitada
            for letra in palavra:
                if letra_adivinhada == letra:
                    palavra_secreta[i] = letra
                i += 1
        #Se não puder, remova uma chance
        else:
            print(f'Opa! Agora você só tem {chances} letra_adivinhadas.')
            chances -= 1
            letras_utilizadas.append(letra_adivinhada)

        #Finalizar jogo caso palavra seja descoberta
        if '_' not in palavra_secreta:
            print(f'Parabéns! Você venceu! A palavra era {palavra}.')
            break
            
    #Finalizar jogo caso chances terminem
    if chances == 0:
        print(f'Que pena! Não foi dessa vez! A palavra era {palavra}.')
        

if __name__ == "__main__":
    game()      
            
        


        


        




    

