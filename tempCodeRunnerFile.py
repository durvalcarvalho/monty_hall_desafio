from random import randint
from random import choice

print("Bem vindo ao simulador do problema de Monty Hall!\n")

#quant_simulacoes = int(input("Digite a quantidade de simulações que você deseja realizar\n"))
quant_simulacoes = 1000

portas = []
for i in range(quant_simulacoes):  #Gera uma matriz com 3 portas em que somente uma delas está com o valor 1.
        porta = [0, 0, 0]
        porta_correta = randint(0, 2)
        porta[porta_correta] = 1

        portas.append(porta)  # Adciona a porta simulada em uma matriz

acertos, erros = 0,0                    #Iniciando acerto e erros igual a 0

for i in range(quant_simulacoes):   #Escolhe um valor, compara com o da porta e contabiliza acertos e erros
    tentativa = randint(0,2)
    if(portas[i][tentativa] == 1):
        acertos = acertos + 1
    else:
        erros = erros + 1

prob_Acertos = float(acertos*100)/float(quant_simulacoes)     #calculando a probabilidade de acertos sem troca de portas
prob_Erros = float(erros*100)/float(quant_simulacoes)         #calculando a probabilidade de acertos sem troca de portas

print("Estatistica de Acertos: {:.1f}%".format(prob_Acertos))
print("Estatistica de Erros: {:.1f}%".format(prob_Erros))
