## Descrição: Esse programa tem como objetivo organizar uma tabela com os placares de um campeonato de PES.
## Entrada: A primeira linha da entrada é um inteiro n que indica a quantidade de times no campeonato. As n linhas seguintes contém os nomes dos times. Após a sequência de times, temos uma sequência de partidas com seus respectivos placares.
## Saída: A saída é a tabela final do campeonato, sendo que cada linha da tabela corresponde aos dados de um time.
## FERNANDO DOS REIS SANTOS FILHO - RA: 23447
#*******************************************************************************
# Funcao: atualizaTabela
#
# Parametros:
#   tabela: uma matriz com os dados da tabela do campeonato
#   jogo: string contendo as informações de um jogo no formato especificado no lab.
#
# Descrição:
#   Deve inserir as informações do parametro 'jogo' na tabela.
#   OBSERVAÇÃO: nesse momento não é necessário ordenar a tabela, apenas inserir as informações.
def atualizaTabela(tabela, jogo):
    jogo = jogo.split() ## Quebra a string de formato "Carlos 3 X 4 Maria"
    jogador1 = jogo[0]
    gol1 = int(jogo[1])
    gol2 = int(jogo[3])
    jogador2 = jogo[4]
    saldo1 = gol1-gol2
    saldo2 = gol2-gol1
    for i in range(len(tabela)):

        if (tabela[i][0]==jogador1): ##Atualiza os dados do Jogador1 da partida
            if(gol1>gol2):
                tabela[i][1] = tabela[i][1] + 3 ##Contabiliza 3 pontos em caso de vitória
            if(gol1==gol2):
                tabela[i][1] = tabela[i][1] + 1 ##Contabiliza 1 ponto em caso de empate
            if(gol1>gol2):
                tabela[i][2] = tabela[i][2] + 1 ##Contabiliza o n. de vitórias

            tabela[i][3] = tabela[i][3] + saldo1 ##Contabiliza o saldo de gols
            tabela[i][4] = tabela[i][4] + gol1 ##Contabiliza o n. de gols pro

        if (tabela[i][0]==jogador2): ##Atualiza os dados do Jogador2 da partida
            if(gol2>gol1):
                tabela[i][1] = tabela[i][1] + 3 ##Contabiliza 3 pontos em caso de vitória
            if(gol1==gol2):
                tabela[i][1] = tabela[i][1] + 1 ##Contabiliza 1 ponto em caso de empate
            if(gol2>gol1):
                tabela[i][2] = tabela[i][2] + 1 ##Contabiliza o n. de vitórias

            tabela[i][3] = tabela[i][3] + saldo2 ##Contabiliza o saldo de gols
            tabela[i][4] = tabela[i][4] + gol2 ##Contabiliza o n. de gols pro

#  -- INSIRA SEU CÓDIGO AQUI -- #
#*******************************************************************************

#*******************************************************************************
# Funcao: comparaTimes
#
# Parametros:
#   time1: informações de um time
#   time2: informações de um time
#
# Descricão:
#   retorna 1, se o time1>time2, retorna -1, se time1<time2, e retorna 0, se time1=time2
#   Observe que time1>time2=true significa que o time1 deve estar em uma posição melhor do que o time2 na tabela.
def comparaTimes(time1, time2):
    if (time1[1]>time2[1]): ##Se o time1 possuir mais pontos do que o time2: time1>time2
        return 1

    elif (time1[1]==time2[1]): ##Se o n. de pontos estiver empatados, mas o n. de vitórias do time1 for maior que o do time2: time1>time2
        if (time1[2]>time2[2]):
            return 1

        elif (time1[2]==time2[2]):
            if (time1[3]>time2[3]): ##... se o n. de vitorias estiver empatado, mas o saldo de gols do time1 for maior que o do time2: time1>time2
                return 1

            elif (time1[3]==time2[3]):
                if (time1[4]>time2[4]): ##... se o saldo de gols estiver empatado, mas o n. de gols pro do time1 for maior que o do time2: time1>time2
                    return 1

    return -1
#  -- INSIRA SEU CÓDIGO AQUI -- #
#*******************************************************************************


#*******************************************************************************
# Funcao: ordenaTabela
#
# Parametros:
#   tabela: uma matriz com os dados da tabela do campeonato.
#
# Descricão:
#   Deve ordenar a tabela com campeonato de acordo com as especificaçoes do lab.
#
def ordenaTabela(tabela):
    for i in range ( 1 , len(tabela)): ##insertionSort Crescente
        aux = tabela[i];
        j=i-1
        verif = comparaTimes(tabela[j], tabela[i])
        while( j >=0 and verif==1 ): #Poe elementos tabela[j]>tabela[i]
            tabela[j+1] = tabela[j]                            #para frente
            j=j-1
            verif = comparaTimes(tabela[j], tabela[i])
        tabela[j+1] = aux #poe tabela[i] na pos. correta

#  -- INSIRA SEU CÓDIGO AQUI -- #
#*******************************************************************************


#*******************************************************************************
# Funcao: imprimeTabela
#
# Parametros:
#   tabela: uma matriz com os dados da tabela do campeonato.
#
# Descrição:
#   Deve imprimir a tabela do campeonato de acordo com as especificações do lab.
def imprimeTabela(tabela):
    for i in reversed(range(len(tabela))): ##Imprimir ao contrário para ficar decrescente
        for j in range (5):
            if (j==4):
                print(tabela[i][j])
            else:
                print(tabela[i][j], end=", ")
#  -- INSIRA SEU CÓDIGO AQUI -- #
#*******************************************************************************
