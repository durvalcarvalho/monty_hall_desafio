from random import randint

print("Bem vindo ao simulador do problema de Monty Hall!\n")
#print("Este programa irá demonstrar que a probabilidade de acertar a porta correta é maior ao trocar as portas")

#quant_simulacoes = int(input("Digite a quantidade de simulações que você deseja realizar\n"))
quant_simulacoes = 5
acertos, erros = 0,0     #Iniciando acerto e erros igual a 0


while(1):
    #Este loop gera todas as portas que serão testadas na simulação
    portas = []
    for i in range(quant_simulacoes):
        porta = [0, 0, 0]
        porta_correta = randint(0, 2)
        porta[porta_correta] = 1

        portas.append(porta)        #Adciona a porta simulada em uma matriz

    for i in range(quant_simulacoes):
        tentativa = randint(0,2)
        if(portas[0][tentativa] == 1 ):
            acertos = acertos + 1
        else:
            erros = erros + 1

    print(acertos)
    print(erros)
    print("Estatistica de Acertos: {}".format(acertos/quant_simulacoes))
    print("Estatistica de Erros: {}".format(erros/quant_simulacoes))

    break
