# Solicita ao usuário que digite o turno de estudo
turno = input("Em que turno você estuda? Digite M para matutino, V para vespertino ou N para noturno: ")

# Verifica o turno e imprime a mensagem correspondente
if turno.upper() == 'M':
    print("Bom dia!")
elif turno.upper() == 'V':
    print("Boa tarde!")
elif turno.upper() == 'N':
    print("Boa noite!")
else:
    print("Valor inválido! Por favor, digite M, V ou N.")
