#Faça um programa que leia a largura e altura de uma parede em metros, calcule a área
#e a quantidade de tinta, necessária para pintá-la, sabendo que cada litro de tinta pinta uma área de 2m²
l = float(input("Digite a largura da parede: "))
a = float(input('Digite a altura da parede: '))
area = float(l*a)
print('É necessário {:.2f} litros para pintar {:.2f}m² de parede!'.format(area/2,area))
