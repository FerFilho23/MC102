## Descrição: Esse programa tem como objetivo executar as funcoes necessarias utilizando os dados dos conjuntos e dos requisitos especificos de cada funcao
## Entrada: A entrada consiste de operações a serem realizadas sobre dois conjuntos nomeados de A e B. Os conjuntos iniciam vazios e cada linha da entrada descreve uma operação a ser realizada sobre um ou entre os dois conjuntos.
## Saída:Cada linha da saída do programa contém o resultado da execução de cada operação dada na entrada, de forma que a saída possui uma linha a menos que a quantidade de linhas da entrada.
## FERNANDO DOS REIS SANTOS FILHO - RA: 23447
#!/usr/bin/env python3

# Funcao: pertence
#
# Parametros:
#   conj: vetor contendo o conjunto de entrada
#    num: elemento a ser verificado pertinencia
#
# Retorno:
#   True se num pertence a conj e False caso contrario
#
def pertence(conj, num):
    # Implementar a funcao e trocar o valor de retorno

    for i in range (len(conj)):
        if (num == conj[i]):
            return True

    return False

# Funcao: contido
#
# Parametros:
#   conj1: vetor contendo um conjunto de entrada
#   conj2: vetor contendo um conjunto de entrada
#
# Retorno:
#   True se conj1 esta contido em conj2 e False caso contrario
#
def contido(conj1, conj2):
    # Implementar a funcao e trocar o valor de retorno
    aux = []

    if (conj1 == []): ## Se o conj1 for vazio ele esta contido em conj2
        return True

    for i in range (len(conj2)):
        if (pertence(conj1, conj2[i])):
                    aux.append(conj2[i])

    if (aux == conj1):
        return True


    return False

# Funcoes: adicao e subtracao
#
# Parametros:
#   conj: vetor contendo o conjunto que tera incluso ou removido o elemento
#    num: elemento a ser adicionado ou removido
#
def adicao(conj, num):
    # Implementar a funcao

    if (pertence(conj, num) != True): ## Se num NAO pertencer a conj, add num a conj
        conj.append(num)
        insertionSortCrescente(conj) ## Ordenar conj crescente



    return conj

def subtracao(conj, num):
    # Implementar a funcao

    if (pertence(conj, num) == True): ## Se num NAO pertencer a conj, remove num a conj
        conj.remove(num)
        insertionSortCrescente(conj) ## Ordenar conj crescente




    return conj

# Funcoes: uniao, intersecao e diferenca
#
# Parametros:
#     conj1: vetor contendo o conjunto de entrada do primeiro operando
#     conj2: vetor contendo o conjunto de entrada do segundo operando
#
# Retorno:
#   Vetor contendo o conjunto de saida/resultado da operacao
#
def uniao(conj1, conj2):
    # Implementar a funcao e trocar o valor de retorno
    aux = []

    for i in range(len(conj1)):
        aux.append(conj1[i])

    for i in range (len(conj2)):
            if (pertence(conj1, conj2[i]) != True):
                aux.append(conj2[i])

    return aux

def intersecao(conj1, conj2):
    # Implementar a funcao e trocar o valor de retorno
    aux = []

    for i in range (len(conj2)):
            if (pertence(conj1, conj2[i]) == True):
                aux.append(conj2[i])

    return aux

def diferenca(conj1, conj2):
    # Implementar a funcao e trocar o valor de retorno
    aux = []

    for i in range (len(conj1)):
            if (pertence(conj2, conj1[i]) != True):
                aux.append(conj1[i])

    return aux

def uniao_disjunta(conj1, conj2):
    # Implementar a funcao e trocar o valor de retorno

    dif1 = diferenca(conj1,conj2)
    dif2 = diferenca(conj2, conj1)

    uniao(dif1, dif2)

    return uniao(dif1, dif2)


def insertionSortCrescente(vet):
    for i in range ( 1 , len(vet)):
        aux = vet[i];
        j=i-1
        while( j >=0 and vet[j]>aux): #Poe elementos v[j]>v[i]
            vet[j+1] = vet[j]         #para frente
            j=j-1

        vet[j+1] = aux #poe v[i] na pos. correta
