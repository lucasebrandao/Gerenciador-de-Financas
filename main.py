
def menu():
    print("\n=== CONTROLADOR DE FINANÇAS ===")
    print("1 - Adicionar transação")
    print("2 - Listar transações")
    print("3 - Ver saldo")
    print("4 - Sair")

def iniciar():

    while True:

        menu()

        opcao = input("Escolha uma opção: ")

        if opcao == "1":
            adicionar_transacao()

        if opcao == "2":
            listar_transacoes()

        if opcao == "3":
            ver_saldo()

        if opcao == "4": 
            break

        else:
            print("Opção inválida.")

iniciar()