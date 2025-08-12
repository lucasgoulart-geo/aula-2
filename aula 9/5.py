"""Faça um Programa que leia 20 números inteiros e armazene-os num vetor. Armazene os números pares no vetor PAR e os números IMPARES no vetor impar. Imprima os três vetores."""

lista_total = []
lista_pares = []
lista_impares = []
for i in range (5):
    n = int(input(f'Digite o {i+1}º número: '))
    lista_total.append(n)
    if n % 2 == 0:
        lista_pares.append(n)
    else:
        lista_impares.append(n)
print(f'A lista de números digitados é: {lista_total}')
print(f'Os numeros {lista_pares}, são pares')
print(f'Já os números{lista_impares}, são impares')