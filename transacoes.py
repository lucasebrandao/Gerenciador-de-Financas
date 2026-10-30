import json
from pathlib import Path


ARQUIVO_DADOS = Path(__file__).resolve().parent / "dados.json"


def carregar_transacoes():
    if not ARQUIVO_DADOS.exists():
        return []

    try:
        with ARQUIVO_DADOS.open("r", encoding="utf-8") as arquivo:
            transacoes = json.load(arquivo)
    except (json.JSONDecodeError, OSError) as erro:
        print(f"Não foi possível carregar os dados: {erro}")
        return []

    if not isinstance(transacoes, list):
        print("O arquivo de dados deve conter uma lista de transações.")
        return []

    return transacoes


def adicionar_transacao(transacoes):
    descricao = input("Insira uma descrição da transação: ").strip()
    if not descricao:
        print("A descrição não pode ficar vazia.")
        return False

    try:
        valor = float(input("Diga o valor da transação: ").replace(",", "."))
    except ValueError:
        print("Valor inválido. Digite um número, como 25,50.")
        return False

    if valor <= 0:
        print("O valor deve ser maior que zero.")
        return False

    print("\nSelecione o tipo de transação: ")
    print("1 - Receita")
    print("2 - Despesa")
    opcao = input("\nOpção: ")

    if opcao == "1":
        tipo = "Receita"
    elif opcao == "2":
        tipo = "Despesa"
    else:
        print("Opção inválida.")
        return False

    transacoes.append({"descricao": descricao, "valor": valor, "tipo": tipo})
    return True


def listar_transacoes(transacoes):
    if not transacoes:
        print("Nenhuma transação foi registrada.")
        return

    for transacao in transacoes:
        print(
            f"{transacao['descricao']} - "
            f"R${transacao['valor']:.2f} - "
            f"{transacao['tipo']}"
        )


def ver_saldo(transacoes):
    saldo = 0
    for transacao in transacoes:
        if transacao["tipo"] == "Receita":
            saldo += transacao["valor"]
        elif transacao["tipo"] == "Despesa":
            saldo -= transacao["valor"]

    print(f"R${saldo:.2f}")


def excluir_transacao(transacoes):
    if not transacoes:
        print("Nenhuma transação foi registrada.")
        return False

    for indice, transacao in enumerate(transacoes):
        print(
            f"\n{indice + 1}) "
            f"{transacao['descricao']} - "
            f"R${transacao['valor']:.2f} - "
            f"{transacao['tipo']}"
        )

    try:
        opcao = int(input("\n\nDigite o índice da transação que deseja excluir: "))
    except ValueError:
        print("Índice inválido. Digite o número de uma transação da lista.")
        return False

    if not 1 <= opcao <= len(transacoes):
        print("Índice fora do intervalo da lista.")
        return False

    del transacoes[opcao - 1]
    return True


def salvar_transacoes(transacoes):
    try:
        with ARQUIVO_DADOS.open("w", encoding="utf-8") as arquivo:
            json.dump(transacoes, arquivo, indent=4, ensure_ascii=False)
    except OSError as erro:
        print(f"Não foi possível salvar os dados: {erro}")


def ver_relatorio(transacoes):
    if not transacoes:
        print("Nenhuma transação foi registrada.")
        return

    receitas = 0
    despesas = 0
    for transacao in transacoes:
        if transacao["tipo"] == "Receita":
            receitas += transacao["valor"]
        elif transacao["tipo"] == "Despesa":
            despesas += transacao["valor"]

    saldo = receitas - despesas
    print(f"Total de receitas: R${receitas:.2f}")
    print(f"Total de despesas: R${despesas:.2f}")
    print(f"Saldo: R${saldo:.2f}")
