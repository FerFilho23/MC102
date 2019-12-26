## Descrição: O objetivo desta tarefa é fazer um programa que use recursividade e que, dada a matriz que descreve a hierarquia de uma empresa, encontre a cadeia hierárquica relativa a um determinado funcionário
## Entrada: A primeira linha contem o numero n, o numero de funcionarios, e k, o identificador numerico do funcionario a ser averiguado sua adeia hierarquica. Em seguida tem-se n linhas correspondentes as linhas da matriz que descreve a hierarquia da empresa
## Saída: Uma lista com os identificadores dos funcionarios da cadeia hierarquica do funcionario k, comecando pelo proprio k e então imprimindo, em ordem crescente por identificador, os outros funcionários
## FERNANDO DOS REIS SANTOS FILHO - RA: 23447

def recursao (matriz, k, hierarquia): ## Funcao recursiva para achar a matriz hierarquia
    for i in range (len(matriz[k])): ## Ler a matriz
         if (int(matriz[k][i]) == 1):
             hierarquia.append(i)
             recursao(matriz, i, hierarquia)

    return

aux1 = input().split(" ") ## Lendo a linha n k

n = int(aux1[0])
k = int(aux1[1])

matriz = []
hierarquia = []
for i in range(n): ## Lendo as linhas individuiais da matriz
    aux2 = input().split(" ")
    matriz.append(aux2) ## Construindo a matriz

recursao(matriz, k, hierarquia) ## Preenche a matriz hierarquia

for i in range (len(hierarquia)):## Ordena hierarquia
    for j in range (len(hierarquia)):
        if (hierarquia[i]<hierarquia[j]):
            hierarquia[i],hierarquia[j] = hierarquia[j], hierarquia[i]

if (len(hierarquia)>0):
    print (k, end=" ")
    for i in range(len(hierarquia)): ## Imprime a hierarquia
        if (i == len(hierarquia)-1):
            print(hierarquia[i])

        else:
            print(hierarquia[i], end=" ")
else:
    print(k)
