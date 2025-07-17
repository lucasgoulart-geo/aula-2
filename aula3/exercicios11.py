#11.	Faça um Programa que peça 2 números inteiros e um número real. Calcule e mostre:
#•	o produto do dobro do primeiro mais metade do segundo .
#•	a soma do triplo do primeiro mais o terceiro.
#•	o terceiro elevado ao cubo.

x = int(input('Digite aqui um numero inteiro: '))
y = int(input('Digite aqui outro numero inteiro: '))
z = float(input('Digite aqui um numero real (aqueles com casas depois da virgula, ex: 1.5): '))

prod1 = (x*2) + (y/2) 
print(f'Resultado do produto um: {prod1:.2f}')

prod2 = (x*3 + x*3 + x*3) + z
print(f'Resultado do produto dois: {prod2:.2f}')

prod3 = z**3
print(f'Resultado do produto três: {prod3:.2f}')