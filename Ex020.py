#Um professor quer sortear um dos seus quatro alunos para apagar o quadro. Faça um programa que ajude ele, lendo o nome
#deles e escrevendo o nomedo escolhido
import random
a1 = input('Digite o nome do aluno 1: ')
a2 = input('Digite o nome do aluno 2: ')
a3 = input('Digite o nome do aluno 3: ')
a4 = input('Digite o nome do aluno 4: ')
#print('{}\n{}\n{}\n{}\n'.format(a1,a2,a3,a4))
lista = [a1,a2,a3,a4] #Cria uma lista com os nomes recebidos
print('O aluno escolhido foi: {}'.format(random.choice(lista))) #Método choice escolha uma opção dentro da lista