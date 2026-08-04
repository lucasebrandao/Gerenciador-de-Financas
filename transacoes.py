import json


def carregar_transacoes():

    arquivo = open("dados.json","r")

    transacoes = json.load(arquivo)

    arquivo.close()

    return transacoes


def adicionar_transacao(transacoes):

    descricao = input("Insira uma descrição da transação: ")
    valor = float(input("Diga o valor da transação: "))

    transacao = {
        'descricao': descricao,
        'valor': valor
    }

    transacoes.append(transacao)


def listar_transacoes(transacoes): 

    for transacao in transacoes:

        print(f"{transacao['descricao']} - R${transacao['valor']:.2f}")

    if not transacoes:
        print("Sem transações registradas.")


def ver_saldo(transacoes):

    saldo = 0

    for transacao in transacoes:
        saldo += transacao['valor']

    print(f"R${saldo:.2f}")


def salvar_transacoes(transacoes):

    arquivo = open("dados.json","w")

    json.dump(transacoes, arquivo, indent=4)

    arquivo.close()