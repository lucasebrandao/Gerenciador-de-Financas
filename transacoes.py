import json


def carregar_transacoes():

    arquivo = open("dados.json","r")

    transacoes = json.load(arquivo)

    arquivo.close()

    return transacoes


def adicionar_transacao(transacoes):

    descricao = input("Insira uma descrição da transação: ")
    valor = float(input("Diga o valor da transação: "))

    print("\nSelecione o tipo de transação: ")
    print("1 - Receita")
    print("2 - Despesa")

    opcao = input("\nOpção: ")

    if opcao == "1":
        tipo = 'Receita'

    if opcao == "2":
        tipo = 'Despesa'
    
    transacao = {
        'descricao': descricao,
        'valor': valor,
        'tipo' : tipo
    }

    transacoes.append(transacao)


def listar_transacoes(transacoes): 

    for transacao in transacoes:

        print(f"{transacao['descricao']} - R${transacao['valor']:.2f} - {transacao['tipo']}")

    if not transacoes:
        print("Sem transações registradas.")


def ver_saldo(transacoes):

    saldo = 0

    for transacao in transacoes:

        if transacao['tipo'] == 'Receita':
            saldo += transacao['valor']

        if transacao['tipo'] == 'Despesa':   
            saldo -= transacao['valor']

    print(f"R${saldo:.2f}")


def excluir_transacao(transacoes):

    if not transacoes:

        print("Nenhuma transação foi registrada.")

    for indice, transacao in enumerate(transacoes):

        print(f"\n{indice + 1}) {transacao['descricao']} - R${transacao['valor']:.2f} - {transacao['tipo']}")

    opcao = int(input("\n\nDigite o índice da transação que deseja excluir: "))
    opcao -= 1
    
    del transacoes[opcao]
    

def salvar_transacoes(transacoes):

    arquivo = open("dados.json","w")

    json.dump(transacoes, arquivo, indent=4)

    arquivo.close()