salario = float(input("Qual o valor do salário do funcionário? R$"))
if salario <= 3000:
    salarioa = (salario * 0.15) + salario
else:
    salarioa = (salario * 0.10) + salario
print("Quem ganhava R$ {:.2f} agora recebe R$ {:.2f}" .format(salario, salarioa))
