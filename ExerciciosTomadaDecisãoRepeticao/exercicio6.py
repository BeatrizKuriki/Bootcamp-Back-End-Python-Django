''''Crie um programa que solicite ao usuário um login e uma senha. 
O programa deve permitir o acesso apenas se o usuário for "admin" e
a senha for "admin123", caso contrário imprima uma mensagem de erro.   '''

print('Vamos logar!!')
usuario = input('Digite o usuário: ')
senha = input('Digite a senha: ')

if usuario == 'admin' and senha == 'admin123':
    print('Login efetuado com sucesso') 
else: print('Senha ou usuário errado, tente novamente!')