print("-*" * 12)
print("Analisador de Triângulos")
print("-*" * 12)
seg1 = float(input("Primeiro segmento: "))
seg2 = float(input("Segundo segmento: "))
seg3 = float(input("Terceiro segmento: "))
if seg1 == seg2 == seg3:
    triangulo = "EQUILÁTERO"
elif seg1 == seg2 != seg3 or seg1 != seg2 == seg3:
    triangulo = "ISÓCELES"
elif seg1 != seg2 != seg3:
    triangulo = "ESCALENO"
print("O triângulo é {}" .format(triangulo))