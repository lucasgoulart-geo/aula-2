"""Faça um programa que leia 5 números e informe o maior número."""

numeros = [10, 45, 3, 99, 23]

# Começamos assumindo que o primeiro número é o maior
maior = numeros[0]

# Percorremos a lista comparando os valores
for numero in numeros:
    if numero > maior:
        maior = numero

print(f'O maior número é:, {maior}')