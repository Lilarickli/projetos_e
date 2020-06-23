# Escreva um algoritmo que obedeça aos seguintes passos (lembre-se de um único algoritmo executa todos os passos a seguir):
#
# Peça ao usuário para que digite um número entre 100 e 100 + X + Y, sendo X e Y seu dia e mês de nascimento, respectivamente.
# Por exemplo, se eu nasci no dia 09/10, pedirei ao usuário para que digite um número entre 100 e 119.
# Se o número digitado não estiver entre esse limite, você deverá pedir novamente por um número válido, repetidamente, até que ele o informe.
# Após receber um número válido, mostre na tela todos os números inteiros entre 1 e o número digitado pelo usuário.
# Se o número for múltiplo de 3, mostre na tela seu nome, em vez do número.
# Se o número for múltiplo de 5, mostre na tela seu sobrenome, em vez do número.
# Se o número for múltiplo de 3 e de 5, mostre na tela seu ano de nascimento, em vez do número.

print("Olá, tudo bem? " +
      "Vamos fazer um pequeno teste?")

nome = input("Qual seu nome: ")
sobrenome = input("E seu sobrenome? ")
dia = int(input("Qual o dia de seu nascimento: "))
mes = int(input("E o mês do seu nascimento: "))
ano = int(input("Só falta o ano do seu nascimento: "))

while (dia < 1 or dia > 31) or (mes < 1 or mes > 12):
    print("Alguma coisa está errada, tente mais uma vez.")
    dia = int(input("Qual o dia de seu nascimento: "))
    mes = int(input("E o mês do seu nascimento: "))

maximo = 100 + dia + mes
numero = int(input("Escolha um número entre 100 e " + str(maximo) + ": "))

while (numero < 100) or (numero > maximo):
    print("Seu número não está entre o valor pedido. Tente mais uma vez.")
    numero = int(input("Escolha um número entre 100 e " + str(maximo) + ": "))

else:
    for numero in range(1, numero + 1):
        if numero % 3 == 0 and numero % 5 == 0:
            print(ano)
        elif numero % 3 == 0:
            print(nome)
        elif numero % 5 == 0:
            print(sobrenome)
        else:
            print(numero)