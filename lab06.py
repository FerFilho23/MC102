## Este programa irá auxiliar no gerenciamento de um estacionamento.
## Entrada: a capacidade c de um estacionamento e o tamanho t dos veiculos que entram e saem (sendo t>0 os veículos entrando e t<0 os veículos saindo).
## Saída: uma mensagem de boas vindas ou volte sempre, caso o veículo esteja entrando ou saindo, e a capacidade restante do estacionamento. Caso o veiculo entrando seja maior que a capacidade do estacionamento o programa imprimira uma mensagem explicitando que o veiculo supera a capacidade maxima.
## FERNANDO DOS REIS SANTOS FILHO - RA: 23447

c = int(input()) # Ler a capacidade inicial
t = 1

while (t!=0): # se t=0 interrompe encerra o programa sem imprimir mais nada
    t=int(input()) #lê o tamanho do veiculo

    if (t>c): #se o veículo maior que a capacidade estiver entrando
        print ("Veiculo muito grande! Capacidade restante:", c)

    if (t<=c) and (t>0): #se o veiculo estiver entrando
        c = c - t
        print ("Seja bem-vindo! Capacidade restante:", c)

    if (t<c) and (t<0):# se o veiculo estiver saindo
        c = c - t
        print ("Volte sempre! Capacidade restante:", c)
