from transacoes import (
    adicionar_transacao,
    carregar_transacoes,
    excluir_transacao,
    listar_transacoes,
    salvar_transacoes,
    ver_relatorio,
    ver_saldo,
)


def menu():
    print("\n=== CONTROLADOR DE FINANÇAS ===")
    print("1 - Adicionar transação")
    print("2 - Listar transações")
    print("3 - Ver relatório")
    print("4 - Ver saldo")
    print("5 - Excluir transação")
    print("6 - Sair")


def iniciar():
    transacoes = carregar_transacoes()

    while True:
        menu()
        opcao = input("\nEscolha uma opção: ")

        if opcao == "1":
            if adicionar_transacao(transacoes):
                salvar_transacoes(transacoes)
        elif opcao == "2":
            print("\n=== TRANSAÇÕES ===\n")
            listar_transacoes(transacoes)
        elif opcao == "3":
            print("\n=== RELATÓRIO ===\n")
            ver_relatorio(transacoes)
        elif opcao == "4":
            print("\n=== SALDO ===\n")
            ver_saldo(transacoes)
        elif opcao == "5":
            if excluir_transacao(transacoes):
                salvar_transacoes(transacoes)
        elif opcao == "6":
            print("\nPrograma encerrado.\n")
            break
        else:
            print("Opção inválida.")


if __name__ == "__main__":
    iniciar()
