## Descrição: Este programa tem como objetivo receber uma mensagem criptografada de um agente infiltrado no imperio. Essa mensagem criptografada tera as coordenadas da base e a elevacao do canhao do imperio, porém estas estarão em palavras chaves. O objetivo do programa é identificar estas palavras chaves dentro uma uma mensagem e obter as informacoes correspondentes.
## Entrada: Uma string contendo a mensagem a ser decifrada
## Saída: Coordenadas
## FERNANDO DOS REIS SANTOS FILHO - RA: 23447


## Ler a mensagem
mensagem = input()
mensagem = mensagem.lower() ##Transformar todas as palavras em letras minusculas
mensagem = mensagem.split() ## Dividir a string em palavras para analisar
## Palavras chaves para decifrar a mensagem
N = "mercurio"
NE = "venus"
L = "terra"
SE = "marte"
S= "jupiter"
SO = "saturno"
O = "urano"
NO = "netuno"

verde = 30
amarelo = 45
vermelho = 60


## Comparar cada palavra da mensagem com os dados para decifrar a mensagem

for i in range (len(mensagem)):
    if (mensagem[i] == N): {
        print ("N -", end =" ") ## Verifica as coordenadas
    }

    if (mensagem[i] == NE): {
        print ("NE -", end =" ")
    }

    if (mensagem[i] == L): {
        print ("L -", end =" ")
    }

    if (mensagem[i] == SE): {
        print ("SE -", end =" ")
    }

    if (mensagem[i] == S): {
        print ("S -", end =" ")
    }

    if (mensagem[i] == SO): {
        print ("SO -", end =" ")
    }

    if (mensagem[i] == O): {
        print ("O -", end =" ")
    }

    if (mensagem[i] == NO): {
        print ("NO -", end =" ")
    }

    ## Verifica as inclinações
    if (mensagem[i] == "verde"): {
        print(verde)
    }
    if (mensagem[i] == "amarelo"): {
        print(amarelo)
    }
    if (mensagem[i] == "vermelho"): {
        print(vermelho)
    }
