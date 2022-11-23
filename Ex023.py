'''Crie um programa que leia o nome completo de uma pessoa e mostre:
o nome com todas as letras maiúsculas
o nome com todas as letras minúsculas
quantas letras ao todo (sem considerar espaços)
quantas letras tem o primeiro nome'''

nome = input('Digite o nome completo: ')
print(nome.upper(), '\n',nome.lower(),)
print('{} tem {} letras ao total!'.format(nome,(len(nome))))
dividido = nome.split() #dividido recebe a lista com as palavras divididas
#print(dividido[0])   Immprime a primeira palavra
print('{} tem {} letras no primeiro nome'.format(nome,len(dividido[0]))) #len(dividido[0] conta quantas letras tem na primeira palavra

