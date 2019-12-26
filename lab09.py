## Descrição: Este programa irá gerar uma matriz NxN e calcular se i é divisor de j ou o contrário. Caso o requisito da divisibilidade seja satisfeito o termo da matriz na posição ixj terá "*" artribuído a ele e "-" caso contrário.
## Entrada: N -> definirá o tamanho da matriz
## Saída: impressão da matriz NxN com seus termos atribuidos "*" ou "-" dependendo da divisibilidade de seus termos i,j representando sua posição na matriz
## FERNANDO DOS REIS SANTOS FILHO - RA: 23447



n = int(input()) ##dimensão da matriz N
cont = 0
linha= [0]
for i in range (n+1): ## Processando as linhas
    if(i<1):
        continue;

    for j in range (n+1): ## Processando as colunas
        if(j<1):
            continue;

        if (j!=n):
            if (i%j==0) or (j%i==0): ## Verifica a divisibilidade das linhas e colunas
                print("*", end=''); ## Imprimir em caso i seja divisor de j ou o contrario
                cont = cont + 1

            else:
                print("-", end=''); ## Caso não satisfaca o criterio acima

        else:
            if (i%j==0) or (j%i==0): ## Verifica a divisibilidade das linhas e colunas
                print("*"); ## Imprimir em caso i seja divisor de j ou o contrario
                cont = cont + 1

            else:
                print("-"); ## Caso não satisfaca o criterio acima



print (cont); ## imprimir o numero de divisores
