'''Crie um programa que leia o nome de uma pessoa e diga se ela tem SILVA'''
nome = str(input('Digite o nome da pessoa: ')).strip().lstrip() #remove os espaços antes e depois do nome
print('Seu nome tem silva? {}'.format('SILVA' in nome.upper()))
