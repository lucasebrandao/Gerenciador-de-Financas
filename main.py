from transacoes import adicionar_transacao, listar_transacoes, ver_saldo, zerar_saldo

def menu():
    print("\n=== CONTROLADOR DE FINANÇAS ===")
    print("1 - Adicionar transação")
    print("2 - Listar transações")
    print("3 - Ver saldo")
    print("4 - Zerar saldo")
    print("5 - Sair")

def iniciar():

    while True:

        menu()

        opcao = input("\nEscolha uma opção: ")

        if opcao == "1":
            adicionar_transacao()

        elif opcao == "2":
            print("\n=== DESPESAS ===\n")
            listar_transacoes()

        elif opcao == "3":
            print("\n=== SALDO ===\n")
            ver_saldo()

        elif opcao == "4":
            zerar_saldo()

        elif opcao == "5": 
            break

        else:
            print("Opção inválida.")

iniciar()