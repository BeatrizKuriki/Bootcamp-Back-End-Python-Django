# Crie um dicionário representando contatos (nome,telefone).
# Permita ao usuário procurar por um contato pelo nome.

contatos = {}

chave = input('Insira o nome do contato: ')
valor = input('Insira o telefone do contato: ')

contatos[chave] = valor

nome = input('Insira o nome do contato que deseja acessar: ')

print(contatos[nome])