"""Faça um Programa que leia um vetor de 10 números reais e mostre-os na ordem inversa."""

lista = [] #aqui nos entramos com a lista
for i in range(10): #solicitamos aqui os 5 valores da lista que está sendo criada
    l = float(input(f'Digite o {i+1}º numero da lista: ')) #aqui pedimos ao usuário para digitar os 5 números da lista
    lista.append(l) #aqui adicionamos cada número digitado a lista sendo, necessáriamente, um número depois do outro
print(f'Lista {lista}')
lista.reverse()

print(f'Lista {lista}')