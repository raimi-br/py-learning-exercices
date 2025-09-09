import math
angulo = float(input("Digite o ângulo desejado: "))
radangulo = math.radians(angulo)
seno = math.sin(radangulo)
cosseno = math.cos(radangulo)
tangente = math.tan(radangulo)
print("O ângulo de ", angulo, "tem o seno de: {:.2f}" .format(seno))
print("O ângulo de ", angulo, "tem o cosseno de: {:.2f}" .format(cosseno))
print("O ângulo de ", angulo, "tem a tangente de: {:.2f}" .format(tangente))