
valor_hora = float(input('Informe o quanto voce recebe por hora em reais: '))
horas_trabalhadas1 = int(input('Informe a quantidade de horas trabalhadas na primeira semana: '))
horas_trabalhadas2 = int(input('Informe a quantidade de horas trabalhadas na segunda semana: '))
horas_trabalhadas3 = int(input('Informe a quantidade de horas trabalhadas na terceira semana: '))
horas_trabalhadas4 = int(input('Informe a quantidade de horas trabalhadas na quarta semana: '))
horas_trabalhadas5 = int(input('Informe a quantidade de horas trabalhadas na quinta semana se houver, caso contrário digite 0: '))

salario = valor_hora * horas_trabalhadas
print(f'o valor do seu salário bruto é de: {salario: 2f}')