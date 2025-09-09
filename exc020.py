import random

print("Digite o nome dos alunos")
aluno1 = str(input("Primeiro aluno:"))
aluno2 = str(input("Segundo aluno:"))
aluno3 = str(input("Terceiro aluno:"))
aluno4 = str(input("Quarto aluno:"))
lista = [aluno1, aluno2, aluno3, aluno4]
random.shuffle(lista)
print("{}" .format(lista))