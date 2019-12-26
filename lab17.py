#!/usr/bin/env python3

import math

## Laboratorio 17 - Banco de Dados Geografico
## Nome: Fernando dos Reis Santos Filho
## RA: 234471
## Descrição: O objetivo deste laboratório é criar uma biblioteca de funções em Python capaz de realizar consultas em um banco de dados geográficos definido
## Entrada: A primeira linha da entrada contém um inteiro n, o número de cidades no banco de dados. A seguir temos n linhas descrevendo cada uma das cidades. Cada linha contém 5 números: x, y, inicio CEP, fim CEP e numero de habitantes.
## Saída: A saída conterá o resultado de cada uma das consultas requisitadas na entrada. A primeira linha da saída de cada consulta contém Consulta X, onde X é o número da consulta, começando em 0.

class Ponto:
    def __init__(self, x, y):
        self.x = x
        self.y = y

class Cidade:
    def __init__(self, coordenadas, inicioCEP, fimCEP, numHabitantes):
        self.coordenadas = coordenadas
        self.inicioCEP = inicioCEP
        self.fimCEP = fimCEP
        self.numHabitantes = numHabitantes

#
# Funcao: distancia
#
# Parametros:
#   a, b: pontos
#
# Retorno:
#   A distancia euclidiana entre a e b.
#
def distancia(c1, c2):
    return int(100 * math.sqrt((c1.x - c2.x)**2 + (c1.y - c2.y)**2)) / 100.0

# Funcao: consulta_cidade_por_cep
#
# Parametros:
#   cidades: lista de cidades (base de dados)
#       cep: CEP desejado
#
# Retorno:
#   O indice da cidade que contem o CEP desejado ou None caso não haja tal cidade.
#
def consulta_cidade_por_cep(cidades, cep):
    # Implementar a funcao e trocar o valor de retorno

    for i in range (len(cidades)):
        if (cidades[i].inicioCEP <= cep and cidades[i].fimCEP >= cep):
            return i

    return None

# Funcao: consulta_cidades_por_raio
#
# Parametros:
#            cidades: lista de cidades (base de dados)
#   cidadeReferencia: indice da cidade referencia (centro da circunferencia)
#               raio: raio da busca
#
# Retorno:
#   Lista dos indices das cidades que estao contidas no raio de busca (incluindo
#   a cidade referencia) *ordenados pelas respectivas distancias da cidade referencia*.
#
def consulta_cidades_por_raio(cidades, cidadeReferencia, raio):
    # Implementar a funcao e trocar o valor de retorno

    listaI = []
    listaD = []


    for i in range(len(cidades)):
        dist = distancia(cidades[i].coordenadas, cidades[cidadeReferencia].coordenadas)
        if (dist <= raio):
            listaD.append(dist)
            listaI.append(i)

    for i in range (len(listaD)):
        for j in range (len(listaD)):
            if(listaD[i]<listaD[j]):
                listaD[i],listaD[j] = listaD[j], listaD[i]
                listaI[i],listaI[j] = listaI[j], listaI[i]


    return listaI

# Funcao: populacao_total
#
# Parametros:
#            cidades: lista de cidades (base de dados)
#   cidadeReferencia: indice da cidade referencia (centro da circunferencia)
#               raio: raio da busca
#
# Retorno:
#   O numero de habitantes das cidades que estao contidas no raio de busca
#
def populacao_total(cidades, cidadeReferencia, raio):
    # Implementar a funcao e trocar o valor de retorno

    lista = consulta_cidades_por_raio(cidades, cidadeReferencia, raio)
    habitantes = 0

    for i in range (len(lista)):
        habitantes += cidades[lista[i]].numHabitantes


    return habitantes

# Funcao: mediana_da_populacao
#
# Parametros:
#            cidades: lista de cidades (base de dados)
#   cidadeReferencia: indice da cidade referencia (centro da circunferencia)
#               raio: raio da busca
#
# Retorno:
#   Mediana do numero de habitantes das cidades que estao contidas no raio de busca
#
def mediana_da_populacao(cidades, cidadeReferencia, raio):
    # Implementar a funcao e trocar o valor de retorno

    habitantes = []

    for i in range(len(cidades)):
        dist = distancia(cidades[i].coordenadas, cidades[cidadeReferencia].coordenadas)
        if (dist <= raio):
            habitantes.append(cidades[i].numHabitantes)

    for i in range (len(habitantes)):
        for j in range (len(habitantes)):
            if(habitantes[i]<habitantes[j]):
                habitantes[i],habitantes[j] = habitantes[j], habitantes[i]
                

    Meio = len(habitantes)//2

    if (len(habitantes)%2 == 0): ##PAR
        return ((habitantes[Meio]+habitantes[Meio-1])/2)

    else:
        return habitantes[Meio] ##IMPAR
