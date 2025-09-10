nome = str(input("Digite seu nome: "))
nome1 = nome[:nome.find(" ")]
nome = nome.split()
print("Seu primeiro nome é: {}" .format(nome1))
print("Seu último nome é: {}" .format(nome[len(nome)-1]))