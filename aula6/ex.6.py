"""Altere o programa anterior permitindo ao usuário informar as populações e as taxas de crescimento iniciais. Valide a entrada e permita repetir a operação."""
while True:
    pop_a = int(input('Digite aqui a população do primeiro pais: '))
    pop_b = int(input('Digite aqui a população do segundo pais: '))
    crescimento_a = float(input('Digite aqui a taxa de crescimento do primeiro pais: '))
    crescimento_b = float(input('Digite aqui a taxa de crescimento do segundo pais: '))
    anos = 0
    while pop_a < pop_b:
        pop_a *= 1 + (crescimento_a / 100)
        pop_b *= 1 + (crescimento_b / 100)
        anos += 1
    print(f'A quantidade de anos para que a populção do país A seja equivalente ao do país B sera de {anos} anos')
    
    sequencia = str(input('Digite (S) para continuar ou (N) para parar o programa: ')).lower()
    if sequencia != 's':
        print('Programa encerrado')
        break