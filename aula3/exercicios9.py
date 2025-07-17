#Faça um Programa que peça a temperatura em graus Farenheit, transforme e mostre a temperatura em graus Celsius. C = (5 * (F-32) / 9).

f = float(input('Digite aqui a temperatura em Farenheit: '))
g = (5 * (f - 32 ) / 9)

print(f'A temperatura convertida em celcius é: {g:.2f}')

