#Faca um programa que peca o tamanho de um arquivo para download (em MB) e a velocidade de
#um link de Internet (em Mbps), calcule e informe o tempo aproximado de download do arquivo
#usando este link (em minutos).

tam = input('Qual tamanho do arquivo em MB para baixar? ')
vel = input('Qual velocidade da internet em Mbps ? ')
tam = int(tam)
vel = int(vel)

print('O arquivo sera baixado em %s min aproximadamente'  %( tam/(vel*60) ))