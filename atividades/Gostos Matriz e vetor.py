# Peça ao usuário para que ele digite um número de jogos de computador (ou console) dos quais gosta.
# Se você não quiser usar como exemplo jogos, pode usar filmes ou bandas de música.

def cria_matriz():
    bandas_num = int(input("Olá! Vamos nos conhecer um pouco. Quantas bandas são suas bandas favoritas? "))
    print("Agora vamos conhecer quais são essas bandas.")

# Após receber o dado, peça para que digite o nome desses jogos (bandas ou filmes), na quantidade indicada.
# Por exemplo, se ele digitou "5", você deve pedir cinco vezes para que ele digite o nome de um jogo/banda/filme.
# Você deve armazenar em um vetor cada um desses itens.
# Caso ele tenha digitado um nome que já está armazenado no vetor, você deve pedir para que informe outro que seja válido.
    matriz = []
    bandas_lista = []
    if bandas_num > len(bandas_lista):
        for i in range(bandas_num):
            while True:
                bandas_nome = input("Qual o nome da " + str(i + 1) + " banda de música favoritas que você pensou? ")
                if bandas_nome in bandas_lista:
                    print("Este nome já foi incluído: " + str(bandas_nome) + ".")
                else:
                    bandas_lista.append(bandas_nome)
                    break

# Após ele ter digitado todos os nomes, peça para que digite a nota que dá para cada um dos itens. A nota deve ser entre 0 e 10.
# Se for abaixo ou acima disso, você deve pedir por uma nova nota. Armazene as notas (válidas) em uma matriz.
# A primeira coluna da matriz deverá ser o nome do item e a segunda, a nota.


        for j in range(bandas_num):
            linha = []
            while True:
                bandas_nota = int(input(("Escolha uma nota de 0 a 10 para a banda " + bandas_lista[j] + ". ")))
                if (bandas_nota < 0) and (bandas_nota > 10):
                    print("Escolha um número entre 0 e 10. ")
                else:
                    linha.append(bandas_lista[j])
                    linha.append(bandas_nota)
                    matriz.append(linha)
                    break

# Mostre a média das notas armazenadas na matriz.
        soma = 0
        for i in range(bandas_num):
            soma = soma + matriz[i][1]

        print("A média das notas atribuidas é: " + str(float(soma / bandas_num))+ ".")

cria_matriz()
