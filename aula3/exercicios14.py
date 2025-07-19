""" João Papo-de-Pescador, homem de bem, comprou um microcomputador para controlar o rendimento diário de seu trabalho. Toda vez que ele traz um peso de peixes maior que 
o estabelecido pelo regulamento de pesca do estado de São Paulo (50 quilos) deve pagar uma multa de R$ 4,00 por quilo excedente. João precisa que você faça um programa que 
leia a variável peso (peso de peixes) e calcule o excesso. Gravar na variável excesso a quantidade de quilos além do limite e na variável multa o valor da multa que João 
deverá pagar. Imprima os dados do programa com as mensagens adequadas.
"""
try:
    peso = float(input('Digite o peso total da pesca em kg: '))
    limite = 50.0
    multa = 4
    excesso = peso - limite
    
    if peso > limite:
        multa_por_kg = excesso * 4
        print(f'O excedente de pesca foi de {excesso}kg, por isso o valor de multa será de R${multa_por_kg: .2f}')

    else:
        print(f'O valor de {limite} está dentro do limite, por isso não será gerada multa.')
except ValueError:
    print('Digite um valor válido')