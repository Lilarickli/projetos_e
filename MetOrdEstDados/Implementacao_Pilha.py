# Em uma biblioteca, um funcionário é responsável por fazer a catalogação de novos livros.
# Esse procedimento acontece toda noite, enquanto os livros são recebidos individualmente durante o dia.
# Sempre que um livro novo é recebido, seu nome é anotado e ele é colocado em cima de uma pilha
# (sempre seguindo a ordem da anotação). À noite, a catalogação dos livros ocorre do último livro recebido
# à tarde até o primeiro livro recebido pela manhã.

def anotar():
    livros_pilha.insert(0, livro)

def catalogar():
    print(livros_pilha)

livros_pilha = []
while True:

    escolha = input(str("Deseja anotar um livro? Digite 1. Se desejar catalogar os livros do dia digite 2. "))

    if escolha == '1':
        livro = input(str("Digite o nome do Livro a ser anotado: "))
        anotar()

    elif escolha == '2':
        catalogar()



# Para testar, cadastre os seguintes livros:
#
# Dom Quixote (Miguel de Cervantes).
# O conde de Monte Cristo (Alexandre Dumas).
# Um conto de duas cidades (Charles Dickens).
# O pequeno príncipe. (Antoine de Saint-Exupéry).
# O senhor dos anéis (J.R.R. Tolkien).
# Na sequência, mostre todos os livros cadastrados.
#
# Entregue o código que desenvolveu e um print da tela com a entrada e saída do teste.