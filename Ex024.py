'''Faça um programa que leia um número de 0 a 9999 e mostre na tela cada um dos dígitos separados'''
numero = int(input("Digite um número de 0 a 9999: "))


unidade = numero // 1 % 10 # divide por um e pega o resto da divisão por 10
dezena = numero // 10 % 10 # divide por dez e pega o resto da divisão por 10
centena = numero // 100 % 10
milhar = numero // 1000 % 10

print('unidade: {}\ndezena: {}\ncentena: {}\nMilhar: {}'.format(unidade, dezena, centena, milhar))