# #1
# # Peça para que o usuário digite um número inteiro maior do que 1.
# # Se o número for maior do que 1, armazene esse valor em um vetor.
#
def determinar_primo():
    numero_lista = []
    while True:
        numero = int(input("Olá. Digite um número maior que 1: "))
        if numero > 1:
            numero_lista.append(numero)


        # Peça por um novo número e assim sucessivamente até que o usuário digite 0.
        # Quando isso acontecer, pare de pedir por novos números.
        elif numero == 0:

            # Mostre na tela quais dos números que ficaram salvos no vetor são primos.
            for numero in numero_lista:
                i = 2
                if numero % i != 0:

                    print("Dos números que você digitou, este é um número primo: " + str(numero))
            break

determinar_primo()

#2
# Faça um algoritmo que solicite ao usuário números e os armazene em um vetor de 20 posições.


def troca_numeros():
    lista_numeros = []
    while len(lista_numeros) < 20:
        numeros = int(input("Preencha a lista com números enquanto for necessário: "))
        lista_numeros.append(numeros)
    # Crie uma função que receba o vetor preenchido e substitua todas as ocorrências de valores negativos por 0,
    # as de valores menores do que 10 por 1 e as demais por 2.
    else:
        for numeros in lista_numeros:
            if numeros < 0:
                print("0")
            elif numeros > 10:
                print("1")
            elif (numeros > 0) and (numeros <= 10):
                print("2")


troca_numeros()
