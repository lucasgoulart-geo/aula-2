"""Faça um Programa que peça a idade e a altura de 5 pessoas, armazene cada informação no seu respectivo vetor. Imprima a idade e a altura na ordem inversa a ordem lida."""
idade1 = []
altura1 = []

for i in range (5):
        idade = int(input(f'Digite aqui a idade da {i+1}º pessoa: '))
        altura = float(input(f'Digite aqui a altura da {i+1}º pessoa: '))
        idade1.append(idade)
        altura1.append(altura)
print(f'A sequencia das idades das pessoas digitadas é {idade1}')
print(f'A sequencia das alturas das pessoas digitadas é {altura1}')
idade1.reverse()
altura1.reverse() 
print(f'A sequencia das idades das pessoas digitadas na ordem inversa é: {idade1}')
print(f'A sequencia das alturas das pessoas digitadas na ordem inversa é: {altura1}')