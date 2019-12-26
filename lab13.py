## Descrição: Este programa tem como objetivo simular o estado de uma determinada população em um apocalipse zumbi a cada dia, segundo as seguintes regras de interacao entre humanos e zumbis. Se X for humano e possuir pelo menos um vizinho zumbi, então X é infectado e se torna um zumbi no dia seguinte;
    ##Se X for humano(1) e possuir pelo menos um vizinho zumbi, então X é infectado e se torna um zumbi no dia seguinte;
    ##Se X for zumbi(2) e possuir dois ou mais vizinhos humanos(1), ele é caçado e morto pelos humanos;
    ##Se X for zumbi(2) e não possuir nenhum vizinho humano(1), ele morre de fome e fica vazio(0) no dia seguinte;
    ##Se X estiver vazio(0) e possuir exatamente dois vizinhos humanos, independente dos demais vizinhos serem zumbis ou vazio, então um humano nasce em X no dia seguinte.
    ##Se nenhuma das alternativas anteriores for verdade, então X permanece como está.
## Entrada: Dois inteiros "m" e "n" representando respectivamente, a linha e a coluna da matriz a ser lida. Um inteiro "i" representando o número de dias a ser analisado. Uma matriz representando o estado da população analisada, esta será preenchida por 0,1 e 2 que representam respectivamente "vazio", "humano" e "zumbi"
## Saída: Para cada dia percorrido será impresso "iteração x", sendo x o número do dia, seguido da matriz que representa o estado da população no respectivo dia.
## FERNANDO DOS REIS SANTOS FILHO - RA: 23447
from copy import deepcopy #função q funciona direito para copia de lista

inteiros = input().split()
m = int(inteiros[0])  ## Le o numero de linhas
n = int(inteiros[1]) ## Le o numero de colunas
dia = int(input()) ## Le o numero de dias

H = 1
Z = 2
vazio = 0

matriz = []
aux = []
V = []

def nvizinhos(matriz, i, j):  ## Verificar o número de vizinhos zumbis, humanos ou vazios dependendo de X
    V = [matriz[i-1][j-1], matriz[i-1][j], matriz[i-1][j+1], matriz[i][j-1], matriz[i][j+1], matriz[i+1][j-1], matriz[i+1][j], matriz[i+1][j+1]]
    global nvizinhosZ; global nvizinhosH; nvizinhosZ= 0; nvizinhosH = 0

    for y in range (8):
        if V[y] == "1":
            nvizinhosH += 1
        elif V[y] == "2":
            nvizinhosZ += 1

    #print("Ponto:",aux[i][j],"Zombie:", nvizinhosZ, "Humanos:", nvizinhosH)   


for i in range (m+2): ## Montando a matriz de entrada
    if i == 0 or i == m+1: ## Adicionar linhas nulas nas extremidades da matriz
        matriz.append(["0"]*(n+2))
    else:
        matriz.append(input().split(" ")) ## numero n de inteiros
        matriz[i].insert(0,"0") ##Fazer a coluna 0 ser nula
        matriz[i].append("0") ##Fazer a coluna n+1 ser nula

aux = deepcopy(matriz)

for k in range (dia+1): ## Simulando o estado da população a cada dia
    if (k!=0):
        for i in range (1,m+1):
            for j in range (1,n+1):
                nvizinhos(matriz, i, j)
                if (matriz[i][j] == "1"):    ## Se X for humano(1) e possuir pelo menos um vizinho zumbi, então X é infectado e se torna um zumbi no dia seguinte;
                    if (nvizinhosZ > 0):
                        aux[i][j] = "2"

                elif (matriz[i][j] == "2"):     ##Se X for zumbi(2) e possuir dois ou mais vizinhos humanos(1), ele é caçado e morto pelos humanos;
                    if (nvizinhosH >= 2 or nvizinhosH == 0):
                        aux[i][j] = "0"                           ##Se X for zumbi(2) e não possuir nenhum vizinho humano(1), ele morre de fome e fica vazio(0) no dia seguinte;

                elif (matriz[i][j] == "0"):         ##Se X estiver vazio(0) e possuir exatamente dois vizinhos humanos, independente dos demais vizinhos serem zumbis ou vazio, então um humano nasce em X no dia seguinte.
                    if (nvizinhosH == 2):
                        aux[i][j] = "1"

        matriz = deepcopy(aux)

    print ("iteracao", k) ## Imprimindo a SAIDA
    for i in range (1,m+1):
        for j in range (1,n+1):
                print(matriz[i][j], end="")
        if not (i == m+1 and j == n):
            print()
