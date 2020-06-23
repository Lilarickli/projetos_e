#Solicitar ao usuário a altura, o comprimento da base e a largura da base.
#UTF-8

print("Insira as dimensões da sua pirâmide:")
altura = int(input("altura: "))
comprimento_base = int(input("comprimento da base: "))
largura_base = int(input("largura da base: "))
area = int(altura*comprimento_base*largura_base)    #Com o comprimento e a largura da base, você conseguirá determinar sua área.

print("Volume=", area*3)    #Volume da pirâmide, multiplicando a área da base pela altura e dividindo o resultado por três.

