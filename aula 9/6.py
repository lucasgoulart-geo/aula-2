"""Faça um Programa que peça as quatro notas de 10 alunos, calcule e armazene num vetor a média de cada aluno, imprima o número de alunos com média maior ou igual a 7.0"""

medias = []
soma = 0
aprovados = 0
for i in range (3):
    for j in range(4):
        nota = float(input(f'Digite a {j+1}º nota do {i+1}º aluno: '))
        soma += nota
    media = soma / 4
    medias.append(media)

    if media >= 7.0:
        aprovados +=1

print(f'A média dos alunos aprovados foi {medias}')
print(f"Número de alunos com média maior ou igual a 7.0: {aprovados}")