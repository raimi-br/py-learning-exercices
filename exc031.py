viag = int(input("Qual a distância da sua viagem? "))
if viag <= 200:
    print("Sua viagem é de {} Km" .format(viag))
    print("O custo será de R$ {:.2f} " .format(viag * 0.5))
else:
    print("Sua viagem é de {} Km" .format(viag))
    print("O custo será de R${:.2f} " .format(viag * 0.45))