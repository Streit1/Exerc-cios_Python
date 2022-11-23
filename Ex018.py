#Faça um programa que leia o comprimento do cateto oposto e do cateto adjacentede um triângulo retângulo
# calcule e mostre o comprimento da hipotenusa
import math
cat_op = float(input('Digite o comprimento do cateto oposto: '))
cat_ad = float(input('Digite o comprimento do cateto adjacente: '))
hyp = math.sqrt((cat_op*cat_op) + (cat_ad*cat_ad))
#Chama a função sqrt(raiz quadrada) do método math
#hyp = math.hypot(cat_op, cat_ad) #Outra solução para o problema
print('O comprimento da hipotenusa é: {:.2f}'.format(hyp))