nome = str(input("Digite seu nome: "))
conferidor = "Silva" in nome
if conferidor is True:
    conferidor = "sim"
else: conferidor = "não"

print("Seu nome tem Silva? {}" .format(conferidor))

