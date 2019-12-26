## Descrição:
## Entrada:
## Saída:
## FERNANDO DOS REIS SANTOS FILHO - RA: 23447

import sys

M = []
I = []
I2 =[]

try:
    arq1=open(sys.argv[1], "r+") ## Abre o arquivo da imagem.pgm
    arq1=arq1.read() ## Le o arquivo imagem
    arq1 = arq1.split("\n")

    for i in range (1, len(arq1)):
        if (i == 2):
            continue

        arq1[i] = arq1[i].split(" ")

        if (i>2 and i<(len(arq1)-1)):
            I = I.append(arq1[i]) ## Criando a matriz imagem

    P2 = arq1[0]
    m = int (arq1[1][0])
    n = int (arq1[1][0])

    ##print (P2, m, n, I)

    arq2=open(sys.argv[2], "r+") ## Abre o arquivo matriz.txt
    arq2=arq2.read() ## Le o arquivo imagem
    arq2 = arq2.split("\n")

    for i in range (1, len(arq2)):
        arq2[i] = arq2[i].split(" ")
        M = M.append(arq2[i]) ## Criando a matriz M

    D = int(arq1[0])
    ##print (D, M)

    for y in range (1, len(I1)-1):
        for x in range (1, len(I1)-1):
            I2[x][y]= Convolusao(M,I1, D, x, y)


    arq.close()
    arq.close()

except:
    print("Arquivo não existe!" )


def Convolusao (M, I1, D, x, y):
    for i in range (3):
        for j in range (3):
            s = int(M[i][j])*int(I1[j-1][i-1])
            return s//D
