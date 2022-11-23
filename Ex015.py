#Escreva um programa que cnverta uma temperatura digitada em ºC e converta em ºF
c = float(input('Informa a temperatura em ºC: '))
f = ((9*c)/5) + 32 #formula de conversão de C para F
print("A temperatura de {:.2f}ºC corresponde a {:.2f}ºF".format(c,f))