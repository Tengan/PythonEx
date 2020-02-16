#Tendo como dado de entrada a altura (h) de uma pessoa, construa um algoritmo que calcule seu
#peso ideal, utilizando as seguintes formulas:
#a. Para homens: (72.7*h) - 58
#b. Para mulheres: (62.1*h) - 44.7
x=input('Digite sua altura, utilizando ponto(.) como virgula: ')

print('Peso ideal para homens: %s' %( (72.7*x)-58 ) )
print('Peso ideal para mulheres: %s' %( (62.1*x)-44.7 ) )