"""Altere o programa anterior para mostrar no final a soma dos números."""


soma = 0
n1 = int(input('Digite aqui o valor do primeiro número: '))
n2 = int(input('Digite aqui o valor do segundo número necessáriamente maior que o primeiro: '))

for i in range(n1+1, n2):
    print(i, end= ' ')
    soma = soma + i

print(f'A soma dos números digitados é {soma}')