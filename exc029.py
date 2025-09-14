vel = int(input("Qual a velocidade do atual do carro? "))
if vel > 80:
    print("VOCÊ EXCEDEU O LIMITE DE 80KM/H E FOI MULTADO EM: R$ {:.2f}" .format((vel - 80) * 7))
else:
    print("Siga bem sua viagem e respeite o limite de velocidade!")