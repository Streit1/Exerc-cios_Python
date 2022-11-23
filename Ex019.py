#Faça um programa que leia um angulo qualquer e mostre na tela o valor do seno cosseno e tangente desse ângulo
#seno eixo vertical, eixo horizontal cosseno
import math
num = float(input('Digite o angulo que você deseja: '))
se = math.sin(math.radians(num)) #math.sin calcula o seno,math.radians(num) calcula o radiano de num, passando como parâmetro um número radiano
co = math.cos(math.radians(num))
ta = math.tan(math.radians(num))
print('O valor do seno é {:.2f}, do cosseno é {:.2f} e o da tangente é {:.2f}'.format(se,co,ta))