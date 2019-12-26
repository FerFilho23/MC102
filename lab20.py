#!/usr/bin/env python3

## Descrição: Nesse laboratório, o objetivo é implementar uma função recursiva que resolve um determinado jogo do Sudoku.
## Entrada: A entrada do programa será de 9x9 dígitos de 0 a 9, onde 0 representa as posições com valores indefinidos que devem ser resolvidas.
## Saída: A saída do programa é composta da grade antes e depois da solução, com separadores - e | para linhas e colunas, respectivamente. Caso não seja encontrada uma solução, o programa irá imprimir Nao foi encontrada uma solucao.. Você pode considerar que todos os testes possuem exatamente uma solução válida.
## FERNANDO DOS REIS SANTOS FILHO - RA: 23447

# Funcao: print_sudoku
# Essa funcao ja esta implementada no arquivo lab20_main.py
# A funcao imprime o tabuleiro atual do sudoku de forma animada, isto e,
# imprime o tabuleiro e espera 0.1s antes de fazer outra modificacao.
# Voce deve chamar essa funcao a cada modificacao na matriz resposta, assim
# voce tera uma animacao similar a apresentada no enunciado.
# Essa funcao nao tem efeito na execucao no Susy, logo nao ha necessidade de
# remover as chamadas para submissao.
from lab20_main import print_sudoku

# O aluno pode criar outras funcoes que ache necessario

# Funcao: resolve
# Resolve o Sudoku da matriz resposta.
# Retorna True se encontrar uma resposta, False caso contrario


def celula(grid, i, j):
        for x in range(i,9):
                for y in range(j,9):
                        if grid[x][y] == 0:
                                return x,y
        for x in range(0,9):
                for y in range(0,9):
                        if grid[x][y] == 0:
                                return x,y
        return -1,-1

def valida(grid, i, j, e):
        linha = all([e != grid[i][x] for x in range(9)])
        if linha:
                coluna = all([e != grid[x][j] for x in range(9)])
                if coluna:
                        secX, secY = 3 *(i//3), 3 *(j//3) 
                        for x in range(secX, secX+3):
                                for y in range(secY, secY+3):
                                        if grid[x][y] == e:
                                                return False
                        return True
        return False

def resolve(resposta, i=0, j=0):
        i,j = celula(resposta, i, j)
        if i == -1:
                return True
        for e in range(1,10):
                if valida(resposta,i,j,e):
                        resposta[i][j] = e
                        if resolve(resposta, i, j):
                                return True
                        # Undo the current cell for backtracking
                        resposta[i][j] = 0
        print_sudoku(resposta)
        return False
