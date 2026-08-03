transacoes = []

def adicionar_transacao():
    descricao = input("Insira uma descrição da transação: ")
    valor = float(input("Diga o valor da transação: "))

    transacao = {
        "descricao": descricao,
        "valor": valor
    }

    transacoes.append(transacao)

def listar_transacoes(): 

    for transacao in transacoes:
        print(f"{transacao['descricao']} - R${transacao['valor']:.2f}")