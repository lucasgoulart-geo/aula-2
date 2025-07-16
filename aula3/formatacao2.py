nome = input('escreva aqui o seu nome ')
print(nome)
altura = float(input('escreva aqui a sua altura '))
peso = float(input('escreva aqui seu peso '))

imc = peso / altura**2
print(f'{nome}, o seu IMC é:{imc: .2f}')