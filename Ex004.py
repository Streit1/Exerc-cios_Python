# Faça um programa que leia algo pela teclado e mostre na tela o seu tipo primitivo e todas as informações possíveis sobre ele
a = input('Digite algo: ')
print('O tipo primitivo desse valor é: ', type(a))
print('Só tem espaços', a.isspace())
print('É um numero', a.isnumeric())
print('É alfabético? ', a.isalpha())
print('é alfanumperico?' , a.isalnum())
print('esta em maiúsculas? ',a.islower())
print('Esta capitalizada? ', a.istitle())#verifica se esta capitalizada (primeira letra maiúscula



