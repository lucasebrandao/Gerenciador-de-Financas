from transacoes import carregar_transacoes, adicionar_transacao, listar_transacoes, ver_saldo, salvar_transacoes, excluir_transacao


transacoes = carregar_transacoes()


def menu():
    print("\n=== CONTROLADOR DE FINANÇAS ===")
    print("1 - Adicionar transação")
    print("2 - Listar transações")
    print("3 - Ver saldo")
    print("4 - Excluir transação")
    print("5 - Sair")

def iniciar():

    while True:

        menu()

        opcao = input("\nEscolha uma opção: ")

        if opcao == "1":

            adicionar_transacao(transacoes)

            salvar_transacoes(transacoes)


        elif opcao == "2":

            print("\n=== TRANSAÇÕES ===\n")

            listar_transacoes(transacoes)


        elif opcao == "3":

            print("\n=== SALDO ===\n")

            ver_saldo(transacoes)


        elif opcao == "4":

            excluir_transacao(transacoes)

            salvar_transacoes(transacoes)

        elif opcao == "5": 

            print("\nPrograma encerrado.\n")

            break


        else:
            print("Opção inválida.")

iniciar()