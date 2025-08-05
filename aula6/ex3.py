"""Faça um programa que leia um nome de usuário e a sua senha e não aceite a senha igual ao nome do usuário, mostrando uma mensagem de erro e voltando a pedir as informações."""
while True:
    login = str(input('Digite o login: '))
    senha = (input('Digite aqui a senha: '))

    if senha == login:
        print('A senha não pode ser igual ao login')
    else:
        print('Usuário cadastrado')
        break
            