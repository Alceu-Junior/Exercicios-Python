npessoas = -1
while npessoas < 0 or not int(npessoas):
    npessoas = int(input("informe o numero de pessoas\n"))
    if npessoas < 0 :
        print("Valor inválido\n") 
          
prcnt = -1
while prcnt < 0 or prcnt > 100:
    prcnt = float(input('informe o percentual do serviço\n'))
    if prcnt > 1:
        prcnt = prcnt / 10
        
total = input("informe o total gasto\n").replace(',','.')
total = float(total)
totalcheio = total + total * prcnt

print(f"O valor total da conta, com a taxa de serviço, será de {totalcheio}")
print(f"Dividindo a conta por {npessoas} pessoa(s), cada pessoa deverá pagar {totalcheio / npessoas}.")



