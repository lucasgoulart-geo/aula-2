"""Faça um programa que leia um vetor de 10 caracteres, e diga quantas consoantes foram lidas. Imprima as consoantes."""

# vetor = []
# total = 0
# for i in range(10):
#     letra = input('Digite uma letra: ')
#     vetor.append(letra)
#     if letra.isalpha() and letra not in 'aeiou':
#         total +=1
#     print(f'Letra {vetor[i]}')
# print(f'A quantidade de consoantes foi: {total}')



# Entrada de uma palavra
palavra = input('Digite uma palavra: ').lower()

# Lista para guardar as consoantes
consoantes = []

# Passa por cada letra da palavra
for letra in palavra:
    # Verifica se é uma letra do alfabeto
    if letra.isalpha():
        # Verifica se NÃO é uma vogal
        if letra != 'a' and letra != 'e' and letra != 'i' and letra != 'o' and letra != 'u':
            consoantes.append(letra)

# Resultado
print(f"\nConsoantes encontradas: {' '.join(consoantes)}")
print(f"Quantidade de consoantes: {len(consoantes)}")