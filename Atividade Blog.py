# UTF-8
# Questão 1

## Crie um algoritmo usando "for" que determine se um número é ou não primo.
# Lembre-se de que os números primos são os números naturais (inteiros e positivos) que somente podem ser divididos por um ou por ele mesmo.
# Você pode ver alguns exemplos de números primos em: https://primes.utm.edu/lists/small/1000.txt.

print("Para saber se um número é primo, insira um número: ")
numero_escolhido = int(input("Número escolhido: "))     #recebe o valor número escolhido

primo = True

for i in range(2, numero_escolhido):
    if (numero_escolhido % i == 0):    #Faz a conta necessária para saber o resto da divisão do número que foi escolhido
        primo = False

if primo == True :
    print(str(numero_escolhido) + " é primo")     #Se o resto da divisão é sempre diferente de 0 no intervalo da divisão, o número escolhido é primo.
else:
    print(str(numero_escolhido) + " não é primo")    #Se o resto da divisão é igual a 0 então não é um número primo, pois pode ser dividido por mais valores fora o 1 ou ele mesmo.


#Questão 2
# Crie um algoritmo usando "while" que determine se um número é ou não primo.

print("Digite um número para saber se ele é ou não primo.")
numero_escolhido = int(input("Digite um número: "))    #recebe um número
i = 2
while (i < numero_escolhido):
    if (numero_escolhido % i == 0):
        print(str(numero_escolhido) + " não é primo.")
        break
    i = i + 1
else:
    print(str(numero_escolhido) + " é primo.")


#Questão 3
# Crie um algoritmo usando "do/while" ("while True") que determine se um número é ou não primo.

print("Digite um número para saber se ele é primo ou não.")
numero_escolhido = int(input("Digite um número: "))
i = 2

while True:
    if numero_escolhido % i == 0:
            print(str(numero_escolhido) + " não é primo.")
    elif numero_escolhido % i != 0:
            print(str(numero_escolhido) + " é primo.")
    if i < numero_escolhido:
        i = i + 1
    break


# Questão 4
# Crie um algoritmo que solicite o peso e a altura de uma pessoa (usando a função "input").
# Com base nesses dois valores, obtenha o Índice de Massa Corporal (IMC) dessa pessoa.
# O IMC é calculado da seguinte forma: IMC = peso/(altura²).
# Mostre na tela o IMC.
#
print("Para saber seu IMC, escreva seu peso e altura: ")
peso = int(input("Peso em KG: "))
altura = str(input("Altura em M: "))
altura = altura.replace(",", ".")
IMC = peso/float(altura)**2
print("IMC: " + str(IMC))

# # Em seguida, mostre qual é a categoria na qual a pessoa se enquadra, como segue:
#
if IMC < 18.5:
    print("Abaixo do peso.")    # Se for menor do que 18,5: "Abaixo do peso".
elif IMC < 25:
    print("Peso Normal.")    # Se for igual ou maior do que 18,5 e menor do que 25: "Peso normal".
elif (IMC > 25) and (IMC < 30):
    print ("Sobrepeso.")    # Se for igual ou maior do que 25 e menor do que 30: "Sobrepeso".
elif (IMC > 30) and (IMC < 35):
    print ("Obesidade I.")    # Se for igual ou maior do que 30 e abaixo de 35: "Obesidade I".
elif (IMC > 35) and (IMC < 40):
    print ("Obesidade II.")    # Se for igual ou maior do que 35 e abaixo de 40: "Obesidade II".
elif IMC > 40:
    print ("Obesidade III.")    # Se for acima de 40: "Obesidade III".

#
# # Questão 5

# Qual foi o exercício mais difícil para você e por quê?

#O exercício mais difícil para mim foram os de determinar qual era o primo. Pois tive que entender o que é que eu precisava saber
# para então montar o código e executar o código.
# O while dentre eles foi o mais difícil, pois eu tive que entender a definição da variável e qual o critério de parada.

# Questão 6
#
# Comparando seu código com os enviados pelos outros colegas, acha que seu código poderia melhorar sob quais aspectos?
#
#
#
# Crie uma nova entrada no blog e compartilhe os algoritmos desenvolvidos, enviando o código-fonte.