import math
import random

print('o professor tem 4 alunos para escolher para apagar o quadro')
a1=str(input('digite o nome do primeiro aluno: '))
a2=str(input('digite o nome do segundo aluno: '))
a3=str(input('digite o nome do terceiro aluno: '))
a4=str(input('digite o nome do quarto aluno: '))
lista=[a1,a2,a3,a4]
escolhido=random.choice(lista)
print('o aluno escolhido foi {}'.format(escolhido))