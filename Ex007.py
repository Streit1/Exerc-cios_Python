##Crie um programa que leia um número e mostre o seu dobro e triplo e raiz quadrada
n = int(input('Digite o valor: '))
raiz = n**(1/2) #Colocado os parênteses para a ordem de precedencia
print('O dobro do número é {}, o triplo é {}, e a raiz quadrada é {:.2f}'.format(2*n,3*n,raiz))
