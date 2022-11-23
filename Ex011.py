#Crie um programa que leia quanto de dinheiro uma pessoa tem na carteira e mostre quantos dólares ela pode comprar
#considere USS 1,00 == R$ 3,27
r = float(input('Digite quantos reais você tem: '))
d = float(3.27)
print('Com R${:.2f}, você pode comprar U$${:.2f}!'.format(r, r/d))