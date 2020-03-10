#Faca um Programa para uma loja de tintas. O programa devera pedir o tamanho em metros
#quadrados da area a ser pintada. Considere que a cobertura da tinta eh de 1 litro para cada 6
#metros quadrados e que a tinta eh vendida em latas de 18 litros, que custam R$ 80,00 ou em
#galoes de 3,6 litros, que custam R$ 25,00.
#Informe ao usuario as quantidades de tinta a serem compradas e os respectivos precos em
#3 situacoes:

#-comprar apenas latas de 18 litros;

#-comprar apenas galoes de 3,6 litros;

#-misturar latas e galoes, de forma que o preco seja o menor. Acrescente 10% de folga e
#sempre arredonde os valores para cima, isto e, considere latas cheias.

x = input('Quantos metros quadrados voce ira pintar? :')

#lata = 18 litros = 6*18 = 108 m2
#galao = 3.6 litros = 6*3.6 = 21,6 m2

qtdLata = x/108
restoLata = x%108
if (qtdLata == 0 and x >= 1  or restoLata>0): #controle Lata
    qtdLata += 1

qtdGalao =int(x/21.6)
restoGalao = x%21.6

if (qtdGalao == 0 and x >= 1  or restoGalao>0): #controle Galao
    qtdGalao += 1

print('Usando apenas Latas de 18 litros, vc ira precisar de %s lata(s), e custara R$ %s' %(qtdLata, qtdLata*80))
print('Usando apenas Galao de 3.6 litros, vc ira precisar de %s galao(oes), e custara R$ %s' %(qtdGalao, qtdGalao*25))

##menor custo com mistura
##Saber quando eh mais viavel um do que o outro

## 4 galoes(R$ 100 e 86,4 m2 ) sai mais caro que 1 lata(R$ 80 e 108 m2)
if ( x>(21.6*3) and qtdLata<1):




####terminar


print('Usando Galoes e Latas, vc ira precisar de %s Galoes e %s Latas, e isso custara R$ %s' %() )