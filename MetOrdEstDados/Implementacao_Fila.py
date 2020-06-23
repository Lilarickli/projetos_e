# Desenvolva um programa em Python que simule um sistema de chamada de clientes.
# Esse sistema deve permitir dois tipos de operação ao usuário:
# a entrada de um novo cliente e a exibição do cliente a ser atendido.
# Essas operações podem ser visualizadas como a inserção de um novo elemento em uma fila e a remoção de um elemento de uma fila.

atendimento = []
while True:
    escolha = input(str("Digite o N para incluir um cliente, S para sair ou P para realizar o atendimento: "))

    if escolha == "N":
        cliente = input(str("Digite o nome do cliente: "))
        atendimento.append(str(cliente))

    elif escolha == "P":
            print(atendimento.pop(0))

    elif escolha == "S":
        list(atendimento)
        break


        # TESTANDO: