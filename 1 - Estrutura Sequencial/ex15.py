#Faca um Programa que pergunte quanto voce ganha por hora e o numero de horas trabalhadas
#no mes. Calcule e mostre o total do seu salario no referido mes, sabendo-se que sao descontados
#11% para o Imposto de Renda, 8% para o INSS e 5% para o sindicato, faca um programa que nos
#de:
#a. salario bruto.
#b. quanto pagou ao INSS.
#c. quanto pagou ao sindicato.
#d. o salario liquido.
#e. calcule os descontos e o salario liquido, conforme a tabela abaixo:

#+ Salario Bruto : R$
#IR (11%) : R$
#INSS (8%) : R$
#Sindicato ( 5%) : R$
#Salario Liquido : R$

#Obs.: Salario Bruto - Descontos = Salario Liquido

ganho=input('Quanto voce recebe por hora ? :' )
horas=input('Quantas horas voce trabalha no mes? :')
total = ganho*horas
ir = (total/100)*11
inss= (total/100)*8
sindicato = (total/100)/5
liquido= total - ir -inss - sindicato

print('Salario bruto : R$ %s'%(total))
print("IR  : R$ %s"%(ir))
print("INSS  : R$ %s" %(inss))
print("Sindicato  : R$ %s"%(sindicato))
print("Salario Liquido : R$ %s"%(liquido)  )