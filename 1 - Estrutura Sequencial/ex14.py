#Joao Papo-de-Pescador, homem de bem, comprou um microcomputador para controlar o
#rendimento diario de seu trabalho. Toda vez que ele traz um peso de peixes maior que o
#estabelecido pelo regulamento de pesca do estado de Sao Paulo (50 quilos) deve pagar uma
#multa de R$ 4,00 por quilo excedente. Joao precisa que voce faca um programa que leia a
#variavel peso (peso de peixes) e calcule o excesso. Gravar na variavel excesso a quantidade de
#quilos alem do limite e na variavel multa o valor da multa que Joao devera pagar. Imprima os
#dados do programa com as mensagens adequadas.


peso = input('Peso do peixe: ')

excedente = peso/50
bool(excedente)
print('excedeu : %s' %(bool(excedente)))
if(bool(excedente)== True):
    print('Excedeu %s kg, e tera que pagar R$ %s de multa' %( (peso%50), (peso%50)*4 ))
