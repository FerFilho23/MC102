## Descrição: Este programa irá simular um sistema de gerenciamento da DAC, realizando operações como impressão, ordenação, inclusão, remoção e busca de alunos matriculados em cada turma.
## Entrada: uma lista com n inteiros (RA de cada aluno) e uma lista de operações a serem realizadas finalizada pelo caractere s.
## Saída:Deverá ser impressa a lista como lida na entrada e, para cada operação 'p' realizada deve ser impressa a lista no estado atual, dadas as operações realizadas anteriormente. Quando o programa ler o operador s, que representa a operação de sair, o programa deve encerrar a execução. No caso da busca binária, os índices da busca para cada passo devem ser impressos, independente do RA estar na lista ou não. Para isso, basta imprimir o índice da posição do meio da lista durante a busca.
## FERNANDO DOS REIS SANTOS FILHO - RA: 23447

from aux import *

def p():
    for i in range (len(lista)-1):
        lista[i]=int(lista[i])
        print (lista[i], end=" ")
    print (lista[len(lista)-1]); ##IMPRIMIR

def inserir(aux):
        lista.append(int(aux))

        if (ordenacao == "c"):
            insertionSortCrescente(lista)
        elif (ordenacao == "d"):
            insertionSortDecrescente(lista)



ordenacao = 0

lista = input().split() ##Le a lista de RAs

while (True):
    aux = input().split()

    if (aux[0] == "s"): ## SAIR do programa
        break;

    if (aux[0] == "p"): ## Executar a função IMPRIMIR
        try:
            p()
        except IndexError:
            continue

    if (aux[0] == "c"): ## Executar a função ORDENACAO CRESCENTE
        try:
            insertionSortCrescente(lista)
            ordenacao = "c"
        except IndexError:
            continue

    if (aux[0] == "d"): ## Executar a função ORDENACAO DECRESCENTE
        try:
            insertionSortDecrescente(lista)
            ordenacao ="d"
        except IndexError:
            continue

    if (aux[0] == "i"): ## Executar a função INSERIR
        inserir(aux[1])

    if (aux[0] == "r"): ## Executar a função REMOVER
        list.remove() ## !!
