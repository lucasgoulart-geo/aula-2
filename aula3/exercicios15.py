""" 15.	Faça um Programa que pergunte quanto você ganha por hora e o número de horas trabalhadas no mês. Calcule e mostre o total do seu salário no referido mês, 
sabendo-se que são descontados 11% para o Imposto de Renda, 8% para o INSS e 5% para o sindicato, faça um programa que nos dê:
•	salário bruto.
•	quanto pagou ao INSS.
•	quanto pagou ao sindicato.
•	o salário líquido.
•	calcule os descontos e o salário líquido, conforme a tabela abaixo:
Salário Bruto : R$ IR (11%) : R$ INSS (8%) : R$ Sindicato ( 5%) : R$ Salário Liquido : R$ Obs.: Salário Bruto - Descontos = Salário Líquido.
"""
valor_hora = float(input('Digite o valor da sua hora de trabalho em reais: '))
horas = int(input('Digite quantas horas voce trabalhou no mês: '))
salario_bruto = horas * valor_hora
ir = salario_bruto * 0.11
inss = salario_bruto * 0.08
sindicato = salario_bruto * 0.05
salario_liquido = salario_bruto - ir - inss - sindicato
descontos = ir + inss + sindicato

print(f'O valor do seu salário bruto é de R${salario_bruto} reais')
print(f'O valor do desconto do imposto de renda é de R${ir} reais')
print(f'O valor do desconto do INSS é de R${inss} reais')
print(f'O valor do desconto do sindicato é de R${sindicato} reais')
print(f'O salário Liquido é de R${salario_liquido: .2f} reais')
print(f' Para resumir: Salário Bruto: R$ IR (11%) : R$ INSS (8%) : R$ Sindicato (5%) : R$ Salário Liquido : R$ Obs.: Salário Bruto: {salario_bruto} - Descontos: {descontos} = Salário Líquido: {salario_liquido: .2f}')


