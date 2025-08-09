"""Faça um programa que leia e valide as seguintes informações:

Nome: maior que 3 caracteres;
Idade: entre 0 e 150;
Salário: maior que zero;
Sexo: 'f' ou 'm';
Estado Civil: 's', 'c', 'v', 'd';
"""
while True:
    nome = str(input('Digite aqui o nome: '))
    if len(nome) > 3:
        break
    print('Nome menor que 3 caracteres')
while True:
    idade = int(input('Digite aqui sua idade: '))
    if 0 <= idade <= 150:
        break
    print('Idade inválida')
while True:
    salario = float(input('Digite aqui seu salário: '))
    if salario > 0:
        break
    print('Salário inválido')
while True:
    sexo = str(input('Digite f para feminimo ou m para masculino: ')).lower()
    if sexo != 'f' or 'm':
        break
    print('Sexo digitado inválido')
while True:
    estado_civil = str(input('Digite aqui S para solteiro, C para casado ou D para divorciado: ')).lower()
    if estado_civil != ['s', 'c', 'd']:
        break
    print('O estado civil digitado está incorreto')

print('Informações cadastradas: ')
print(f'Nome: {nome}')
print(f'Idade: {idade}')
print(f'Salário: R${salario:.2f}')
print(f'Sexo: {'Feminino' if sexo == 'f' else 'Masculino'}')
print(f'Estado Civil: {estado_civil.upper()}')

    
