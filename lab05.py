## Este programa irá calcular, dado o tempo maximo em segundos e a quantidade de combustivel, se uma nave terá combustivel suficiente, dentro do tempo limite, de fugir de uma situacao de perigo.
## FERNANDO DOS REIS SANTOS FILHO - RA: 23447

t = int(input()) ## tempo
c = int(input()) ## qntd necessaria de combustivel
x = input () ## lendo a lista de antimateria e combustivel
x = x.split(" ")
soma = 0
for i in range (t):
    soma = soma + int(x[i])
    if (soma >= c):
        print ("sim")
        print (i+1)
        break;

if(soma<c):
    print ("nao")
    print (i+2)
