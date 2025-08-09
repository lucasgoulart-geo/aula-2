"""Faça um programa que, dado um conjunto de N números, determine o menor valor, o maior valor e a soma dos valores."""

qtnumero = int(input('Digite a quantidade de números desejada: '))
lista = []
for i in range (qtnumero):
    numero = int(input(f'informe o {i +1}º numero: '))
    lista.append(numero)
print(f'Sua lista contém os seguintes números {lista}')