# Tendo como dado de entrada a altura (h) de uma pessoa, construa um algoritmo que calcule seu peso ideal, utilizando as seguintes fórmulas:
#•	Para homens: (72.7*h) - 58
#•	Para mulheres: (62.1*h) - 44.7


sexo = input('Qual o seu sexo? responda com mulher ou homem: ')
altura = float(input('Qual a sua altura? '))

if sexo == 'mulher':
    pm = (62.1 * altura) - 44.7
    print(f'O seu peso ideal é: {pm:.2f}')

else:
    ph = (72.7 * altura) - 58 
    print(f'O seu peso ideal é: {ph:.2f}')


