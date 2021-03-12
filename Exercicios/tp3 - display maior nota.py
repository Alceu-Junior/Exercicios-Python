maiornota = 0
vencedor = ' '
for i in range(1, 6):
    nome = input(f'informe o nome do {i}º participante\n')
    nota = -1
    while nota < 0 or nota > 10:
        nota = float(input(f'informe a nota do {i}º participante\n'))
        if nota < 0 or nota > 10:
            print('A nota precisa ser um valor entre 0 e 10')
    if nota > maiornota:
        maiornota = nota
        vencedor = nome
    
print(f'O(a) vencedor(a) foi {vencedor} com nota {maiornota}!')
    
