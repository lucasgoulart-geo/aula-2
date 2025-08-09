"""Faça um programa que leia uma lista de 10 números e os mostre em ordem inversa"""


lista = []
for i in range (4):
    numero = int(input(f'informe o {i +1}º numero: '))
    lista.append(numero)
print('Ordem de entrada')
print(lista)
print('Ordem inversa')
lista.reverse()
print(lista)
print(f'o maior número da lista é {max(lista)}')
print(f'o menor número da lista é {min(lista)}')
print('Ordenando a lista')
print(f'ordenação: {sorted(lista)}')
print('Ordem inversa')
lista.reverse
print(lista)