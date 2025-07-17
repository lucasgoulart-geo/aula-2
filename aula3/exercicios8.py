
valor_hora = float(input('Informe o quanto voce recebe por hora em reais: '))
ht1 = int(input('Informe a quantidade de horas trabalhadas na primeira semana: ')) # ht1 = horas trabalhadas na semana 1
ht2 = int(input('Informe a quantidade de horas trabalhadas na segunda semana: ')) # ht2 = horas trabalhadas na semana 2
ht3 = int(input('Informe a quantidade de horas trabalhadas na terceira semana: ')) # ht3 = horas trabalhadas na semana 3
ht4 = int(input('Informe a quantidade de horas trabalhadas na quarta semana: ')) # ht4 = horas trabalhadas na semana 4
ht5 = int(input('Informe a quantidade de horas trabalhadas na quinta semana se houver, caso contrário digite 0: ')) # ht5 = horas trabalhadas na semana 5

salario = (ht1 + ht2 + ht3 + ht4 + ht5) * valor_hora
print(f'o valor do seu salário bruto é de: {salario: .2f}')