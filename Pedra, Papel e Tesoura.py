# Peça ao usuário digitar uma opção: 1 equivale a papel, 2 equivale à pedra e 3 equivale à tesoura.
# Se ele digitar qualquer valor que não seja um desses valores, sairá do jogo.



def jogo():
    resultado_geral = []
    opcoes = ["Papel", "Pedra", "Tesoura"]
    print("Vamos jogar Pedra, Papel e Tesoura? \n  Considere: \n 1 - Papel \n 2 - Pedra \n 3 - Tesoura")
    while True:
        opcao = int(input("Escolha uma dessas opções, digite o número correspondente à opção escolhida para jogar.\n"
                          "Ou qualquer outra tecla para encerrar."))
        if (opcao <= 0) or (opcao >= 4):
            print("Você escolheu encerrar o jogo.")
            resultado_final(resultado_geral)
            break
        else:
            comp = random.randint(1, 3)
            print("Sua escolha foi: " + opcoes[opcao - 1] + " O computador escolheu: " + opcoes[comp - 1])
            resultado_partida(opcao, comp, resultado_geral)

            # Assim que ele digitar uma jogada, gere um número aleatório entre 1 e 3.
            # Depois de mostrar o resultado, peça por uma nova opção (item 1).
            # Quando o usuário escolher sair do jogo (isto é, quando ele digitar qualquer opção que não seja 1, 2 ou 3),
            # mostre na tela quantas vezes jogou contra o computador.


def resultado_partida(opcao, comp, resultados):
    J = str("Jogador")
    C = str("Computador")
    E = str("Empate")
    if (opcao == int(comp)):  # mostra na tela se houve um empate, se o usuário ganhou ou se o computador ganhou.
        print("Você empatou no jogo.")
        resultados.append(str(E))
    elif (opcao == 3 and comp == 1):
        print("Você venceu.")
        resultados.append(str(J))
    elif (opcao == 1 and comp == 3):
        print("Você perdeu.")
        resultados.append(str(C))
    elif (opcao < int(comp)):
        print("Você venceu.")
        resultados.append(str(J))
    elif (opcao > int(comp)):
        print("Você perdeu.")
        resultados.append(str(C))
    # Para cada partida feita, armazene em um vetor os resultados.
    # Precisamos armazenar no vetor quem foi o vencedor de cada partida (ou se houve um empate).
    return resultados

def resultado_final(resultado_p):    # Quando o usuário escolher terminar a partida, mostre a porcentagem de partidas em que ele venceu e a porcentagem de empates.
    print(resultado_p)
    quantidade_jogos = len(resultado_p)
    jogador_vence = resultado_p.count("Jogador")*100/quantidade_jogos
    print("Você venceu " + str(jogador_vence) + " % das jogadas.")
    computador_vence = resultado_p.count("Computador")*100/quantidade_jogos
    print("O Computador venceu " + str(computador_vence) + " % das jogadas.")
    empates = resultado_p.count("Empate")*100/quantidade_jogos
    print(str(empates) + " % das jogadas foram empates.")


import random
jogo()

# Modifique seu código para que haja pelo menos uma função responsável por mostrar o menu (isto é, o item 1 da primeira fase do projeto final),
# uma função para determinar o resultado da partida (item 3 da primeira fase)
# e uma função para mostrar o resultado de todas as partidas (item 2 da segunda fase).




