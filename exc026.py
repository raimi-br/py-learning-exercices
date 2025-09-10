frase = str(input("Digite uma frase: ")).lower()
frase = frase.strip()
contara = frase.count('a')
primeiroa = frase.find('a') + 1
ultimoa = frase.rfind('a') +1
print("A frase {}" .format(frase), " têm {}" .format(contara), " letras 'A'")
print("A primeira aparição da letra 'A' é na posição {}" .format(primeiroa))
print("A última aparição da letra 'A' é na posição {}" .format(ultimoa))
