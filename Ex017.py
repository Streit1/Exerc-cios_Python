#Crie um programa que leia um número real qualquer pelo teclado e mostre na tela a sua porção inteira
from math import trunc
n = float(input('Digite um número real: '))
print('A porção inteira de {} é {}'.format(n, trunc(n)))#math.trunc(n) chama a função trunc da biblioteca math para a variável n