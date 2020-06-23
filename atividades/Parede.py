#cálculo de quantas latas de tinta são necessárias para pintar uma parede
#UTF-8

print("Para saber quantas latas de tinta são necessárias insira o altura e comprimento de sua parede em metros:")

altura = int(input("altura: "))    #recebe valor altura
comprimento = int(input("comprimento: "))    #recebe valor comprimento
latas_tinta = int(altura*comprimento) / float(3/4)    #multiplica área e divide por 1,5 latas de tinta para cada m2



print(latas_tinta, "Latas de tinta serão necessárias") #reultado



