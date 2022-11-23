#Escreva um programa que receba um valor em metros e exiba o valor convertido em centímetros e milimetros
n = float(input('Digite a medida em metros: '))
print('{} metros, possui {:.2f} centímetros e {:.2f} milimetros'.format(n,n*100,n*1000))