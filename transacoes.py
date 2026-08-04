import json

arquivo = "dados.json"

def carregar_transacoes():
    with open("dados.json","r") as arquivo:

# CONTINUAR A IMPLEMENTAR SALVAMENTO DAS TRANSAÇÕES COM JSON.

transacoes = []

def adicionar_transacao():

    descricao = input("Insira uma descrição da transação: ")
    valor = float(input("Diga o valor da transação: "))

    transacao = {
        'descricao': descricao,
        'valor': valor
    }

    transacoes.append(transacao)

def listar_transacoes(): 

    for transacao in transacoes:

        print(f"{transacao['descricao']} - R${transacao['valor']:.2f}")

    if not transacoes:
        print("Sem transações registradas.")

def ver_saldo():

    saldo = 0

    for transacao in transacoes:
        saldo += transacao['valor']

    print(f"R${saldo:.2f}")