from random import randint

print("Bem vindo ao simulador do problema de Monty Hall!\n")
#print("Este programa irá demonstrar que a probabilidade de acertar a porta correta é maior ao trocar as portas")

#quant_simulacoes = int(input("Digite a quantidade de simulações que você deseja realizar\n"))
quant_simulacoes = 5
acertos, erros = 0,0                    #Iniciando acerto e erros igual a 0

while(1):                               #Este loop gera todas as portas que serão testadas na simulação
    portas = []
    acertos = 0
    erros = 0

    for i in range(quant_simulacoes):   #Gera uma porta, adciona um valor e armazena em uma matriz
        porta = [0, 0, 0]
        porta_correta = randint(0, 2)
        porta[porta_correta] = 1

        portas.append(porta)            #Adciona a porta simulada em uma matriz

    for i in range(quant_simulacoes):   #Escolhe um valor, compara com o da porta e contabiliza acertos e erros
        tentativa = randint(0,2)
        if(portas[0][tentativa] == 1 ):
            acertos = acertos + 1
        else:
            erros = erros + 1

    prob_Acertos = acertos*100/quant_simulacoes     #calculando a probabilidade de acertos
    prob_Erros = erros*100/quant_simulacoes         #calculando a probabilidade de acertos

    for i in range(quant_simulacoes):
        tentativa = randint(0,2)
        for i in range(3):                          #encontrando a posição da resposta certa
            portas[0][i] = 1
            posicao_porta_certa = i
        posibilidades = [0,1,2]                     #este vetor são as possibilidades de escolha
        posibilidades = [x for x in posibilidades if x != tentativa and x != posicao_porta_certa] #Estou removendo a porta correta e a porta escolhida, irei usar a posição restante para "abrir" (está seria a porta incorreta que é apresentada para o usuário antes de oferer a posibilidade de mudança de escolha)
        print(posibilidades)                        #lembrar do caso especial quando a escolha do jogador também é a escolha correta


    break

    #print("Estatistica de Acertos: {}%".format(prob_Acertos))
    #print("Estatistica de Erros: {}%".format(prob_Erros))
