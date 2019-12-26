## Descrição: Este programa irá criar e carregar uma base de dados sobre os monstros do jogo PokéaMãe.Com base nesses dados coletados o programa irá calacular o ponto de combate futuro (PCf) das evoluções das espécies de monstros
## Entrada: N -> número de evoluções de monstros da base de dados; I-> identificador da espécie; PCa -> poder antes da evolção; PCf -> poder futuro conhecido
## Saída:PCf estimado das evoluções dos monstros
## FERNANDO DOS REIS SANTOS FILHO - RA: 23447

import math
N = int(input())
lista_ID=[]
multp=[]
ID_novo=1
PCa_novo=1
soma_multp=[] ## soma dos multiplicadores
num_multp=[] ## numero total de multiplicadores - usar para fazer a média do multp. pra cada especie

for i in range (N):

    linha = input()
    ints = [int(i) for i in linha.split()]
    ID = ints[0]
    PCa = ints[1]
    PCf = ints[2]

    if ID not in lista_ID: ## Ao encontrar um ID novo, add ele na lista do banco de dados
        lista_ID.append(ID)
        soma_multp.append(0)
        num_multp.append(0)

    for j in range (len(lista_ID)): ## Ao encontrar um ID conhecido, calcular o seu multp.
        if (ID == lista_ID[j]):
            soma_multp[j]+= PCf/PCa
            num_multp[j]+=1

while (ID_novo!=0) and (PCa_novo!=0): ## Após criar o banco de dados, calcular o PCf dos monstros dados
    linha = input()
    ints = [int(i) for i in linha.split()]
    ID_novo = ints[0]
    PCa_novo = ints[1]
    for i in range (len(lista_ID)):
        if (ID_novo == lista_ID[i]):
            media_multp = soma_multp[i]/num_multp[i] ##Calcula a média dos multp
            PCf_novo = math.ceil(PCa_novo*media_multp) ## Calcula o PCf_novo
            print(PCf_novo);
