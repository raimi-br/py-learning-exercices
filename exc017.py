import math
catop = float(input("Digite o valor do cateto oposto: "))
catadj = float(input("Digite o valor do cateto adjacente: "))
print("O valor da hipotenusa dos catetos é: {:.2f}".format(math.hypot(catop, catadj)))
