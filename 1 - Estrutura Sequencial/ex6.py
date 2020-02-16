#Faca um Programa que peca o raio de um circulo, calcule e mostre sua area. usando pi=3,14
raio=input('Raio do circulo: ')
print(raio**2) # usando duas vezes o asterisco, o python entende que nao eh mais multiplicacao e sim potencia
area = 3.14 *(raio**2)
print ('Area = %s cm^2'%(area))