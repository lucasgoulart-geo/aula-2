"""Faça um Programa que leia um vetor de 5 números inteiros e mostre-os."""

lista = [] #aqui nos entramos com a lista
for i in range(5): #solicitamos aqui os 5 valores da lista que está sendo criada
    l = int(input(f'Digite o {i+1}º numero da lista: ')) #aqui pedimos ao usuário para digitar os 5 números da lista
    lista.append(l) #aqui adicionamos cada número digitado a lista sendo, necessáriamente, um número depois do outro

for i in range(5):
    print(f'a posição -> {i} tem o conteúdo {lista[i]}') #fazendo desse jeito conseguimos retirar o identificar o número do item e depois a contagem da lista.
    