idade = -1
while idade < 0:
    idade = int(input('informe sua idade: '))

if idade > 18 and idade < 70:
    print('Tem obrigação de votar')
elif idade < 16:
   print("Não tem direito a voto.")
else:
    print("Não tem obrigação de votar.")

