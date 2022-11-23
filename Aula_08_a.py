import math #importa todas as funcionalidades da biblioteca math
num =int(input('Digite um número: '))
raiz = math.sqrt(num)#raiz recebe a raiz quadrada de num
print ('A raiz quadrada de {} é {}'.format(num,math.ceil(raiz)))#math.ceil arredonda o valor para cima