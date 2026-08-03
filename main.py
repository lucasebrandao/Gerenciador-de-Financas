from transacoes import adicionar_transacao, listar_transacoes

def menu():
    print("\n=== CONTROLADOR DE FINANÇAS ===")
    print("1 - Adicionar transação")
    print("2 - Listar transações")
    print("3 - Ver saldo")
    print("4 - Sair")

def iniciar():

    while True:

        menu()

        opcao = input("\nEscolha uma opção: ")

        if opcao == "1":
            adicionar_transacao()

        elif opcao == "2":
            print("\n=== Despesas ===\n")
            listar_transacoes()

        elif opcao == "3":
            ver_saldo()

        elif opcao == "4": 
            break

        else:
            print("Opção inválida.")

iniciar()