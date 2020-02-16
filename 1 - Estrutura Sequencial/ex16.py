import math
#Faca um programa para uma loja de tintas. O programa devera pedir o tamanho em metros
#quadrados da area a ser pintada. Considere que a cobertura da tinta eh de 1 litro para cada 3
#metros quadrados e que a tinta eh vendida em latas de 18 litros, que custam R$ 80,00. Informe ao
#usuario a quantidades de latas de tinta a serem compradas e o preco total.
x = input ('Quantos metros quadrados sera pintado : ')

# 3 metroQuad = 1 Litro
# 1 Lata = 18 Litros
# 1 Lata = 54 metroQuad
zero = 0
um = 1 

qtdLata = x/54
resto = x%54

if (qtdLata == zero and x >=um  or resto>0):
    qtdLata += 1

print("sera necessaria %s lata(s)" %(qtdLata))
print("O valor total eh de  R$ %s,00 "%(qtdLata*80))