import random

print("=+" * 30)
print("Vou pensar em um número entre 0 e 5, tente adivinhar qual...")
print("=+" * 30)
numeros = [0, 1, 2, 3, 4, 5]
gerador = random.choice(numeros)
numeroadv = int(input("Tente adivinhar: "))
print("Gerando...")
if numeroadv == gerador:
    print("Parabéns você acertou!")
    print("Número digitado: {}" .format(numeroadv))
    print("Número pensado: {}" .format(gerador))
elif numeroadv == str:
    print("Você digitou uma letra")
else:
    print("Que pena, você errou!")
    print("Número digitado: {}" .format(numeroadv))
    print("Número pensado: {}" .format(gerador))
