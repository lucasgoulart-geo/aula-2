"""Faça um Programa que leia um vetor de 5 números inteiros, mostre a soma, a multiplicação e os números."""
vetor = []
soma = 0
multiplicacao = 1
for i in range (5):
    vetores = int(input(f'Digite aqui o {i+1}º valor selecionado: '))
    soma += vetores
    multiplicacao *= vetores
    vetor.append(vetores)
print(f'Os valores digitados foram: {vetor}')
print(f'A soma dos valores digitados foi {soma}')
print(f'A multiplicação dos valores digitados é {multiplicacao}')