## Este programa irá calcular se é possivel balancear as cargas dadas como entrada em dois lotes separados de igual peso.

## FERNANDO DOS REIS SANTOS FILHO - RA: 23447



c1=int(input()) ## Ler o peso das cargas individuais
c2=int(input())
c3=int(input())
c4=int(input())

a=c2+c3+c4 #C1
b=c3+c4+c1 #C2
c=c4+c1+c2 #C3
d=c1+c2+c3 #C4
e=c3+c4 #C1+C2
f=c2+c4 #C1+C3
g=c2+c3 #C1+C4
h=c1+c4 #C2+C3
i=c1+c3 #C2+C4
j=c1+c2 #C3+C4

c1c2 = c1+c2
c1c3 = c1+c3
c1c4 = c1+c4
c2c3 = c2+c3
c2c4 = c2+c4
c3c4 = c3+c4

if (c1 == a): ## Testar as possibilidades de se dividir o lote de cargas em duas partes de massa igual 
    print ("sim")
elif (c2 == b):
    print ("sim")
elif (c3 == c):
    print ("sim")
elif (c4 == d):
    print ("sim")
elif (c1c2 == e):
    print ("sim")
elif (c1c3 == f):
    print ("sim")
elif (c1c4 == g):
    print ("sim")
elif (c2c3 == h):
    print ("sim")
elif (c2c4 == i):
    print ("sim")
elif (c2c4 == j):
    print ("sim")
else:
    print ("nao")
