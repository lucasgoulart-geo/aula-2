"""Faça um programa que receba dois números inteiros e gere os números inteiros que estão no intervalo compreendido por eles."""
n1 = int(input('Digite aqui o valor do primeiro número: '))
n2 = int(input('Digite aqui o valor do segundo número necessáriamente maior que o primeiro: '))

for i in range(n1+1, n2):
    print(i, end= ' ')