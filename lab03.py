
## Este programa irá determinar se é possivel abastecer os postos de combustível tendo como entrada o diametro e o coprimento do tanque de um caminhão.


## FERNANDO DOS REIS SANTOS FILHO - RA: 23447


d = float(input()) ## lê diametro
h = float(input()) ## lê comprimento
a = float(input()) ## Postos de A até C
b = float(input())
c = float(input())

r=d/2 ## calcula raio
V=3.14*r*r*h*1000 ## calcula volume

if (V>=a):
  print("posto A foi reabastecido")
  V = V-a
else:
    print("posto A nao foi reabastecido")

if (V>=b):
  print("posto B foi reabastecido")
  V = V-b

else:
  print("posto B nao foi reabastecido")

if (V>=c):
  print("posto C foi reabastecido")
  V = V-b

else:
  print("posto C nao foi reabastecido")
