#Faça um programa que leia o nome de quatro alunos e sorteie aordem de apresentação mostrando os nomes em ordem
import random
a1 = input('Digite o nome do aluno 1: ')
a2 = input('Digite o nome do aluno 2: ')
a3 = input('Digite o nome do aluno 3: ')
a4 = input('Digite o nome do aluno 4: ')
#print('{}\n{}\n{}\n{}\n'.format(a1,a2,a3,a4))
lista = [a1,a2,a3,a4] #Cria uma lista com os nomes recebido
random.shuffle(lista) #Mistura os elementos da lista
print('A ordem escolhida foi: {}'.format(lista)) #Método choice escolha uma opção dentro da lista