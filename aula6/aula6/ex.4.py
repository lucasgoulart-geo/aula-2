"""Supondo que a população de um país A seja da ordem de 80000 habitantes com uma taxa anual de crescimento de 3% e que a população de B seja 200000 habitantes com uma 
taxa de crescimento de 1.5%. Faça um programa que calcule e escreva o número de anos necessários para que a população do país A ultrapasse ou iguale a população do país B,
 mantidas as taxas de crescimento."""

pop_a = 80000
pop_b = 200000
anos = 0
while pop_a < pop_b:
    pop_a *= 1.03
    pop_b *= 1.015
    anos += 1
print(f'A quantidade de anos para que a populção do país A seja equivalente ao do país B sera de {anos} anos')