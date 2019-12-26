## Este programa irá simular uma luta entre dois personagens de um jogo de luta
## Entrada: Vários números inteiros que irão representar os golpes dados (positivos) e os golpes recebidos (negativos) por um lutador. O round termina quando os ponrtos de vida de um lutador são  PV <=0
## Saída: "nome do lutador: PV - soma = PVnovo"
## FERNANDO DOS REIS SANTOS FILHO - RA: 23447

PVRyu = 50 ## Pontos de vida (PV) de Ryu e Ken
PVRyu_Novo = 50
PVKen = 50
PVKen_Novo = 50
RoundKen = 0 ## No. de Rounds vencidos
RoundRyu = 0
dano = 0
combo = 0

dano = int(input()) ## Ler e Contabilizar os danos da sequencia de golpes

while (PVRyu >= 0) and (PVKen >= 0): ## ROUND 1
    if (dano>0):
        while (dano>0) and (PVKen_Novo >= 0):
            combo = combo - dano
            PVKen_Novo = PVKen_Novo - dano
            dano = int(input())

        print ("Ken: ", PVKen, " - ", abs(combo), " = ", PVKen_Novo)
        PVKen = PVKen_Novo


    elif (dano<0):
        while (dano<0) and (PVRyu_Novo >= 0):
            combo = combo + dano
            PVRyu_Novo = PVRyu_Novo + dano
            dano = int(input())

        print ("Ryu: ", PVRyu, " - ", abs(combo), " = ", PVRyu_Novo)
        PVRyu = PVRyu_Novo

    combo = 0

if (PVKen < 0):
    RoundRyu = RoundRyu + 1

if (PVRyu < 0):
    RoundKen = RoundKen + 1


if (RoundKen == 1 ) and (RoundRyu == 1): ##empate
    print ("empate")

if (RoundKen == 2): ## imprimir a vitoria
    print ("Ken venceu")

if (RoundRyu == 2):
    print ("Ryu venceu")
