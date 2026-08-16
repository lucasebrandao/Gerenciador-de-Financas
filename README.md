# Gerenciador de Finanças

Projeto desenvolvido em Python para praticar lógica de programação, organização de código e manipulação de dados.

O programa permite gerenciar transações financeiras, possibilitando cadastrar receitas e despesas, visualizar movimentações, calcular saldo e manter os dados salvos mesmo após fechar a aplicação utilizando arquivos JSON.

## Funcionalidades

* Adicionar transações financeiras;
* Classificar transações como receita ou despesa;
* Visualizar transações cadastradas;
* Calcular saldo atual;
* Remover transações;
* Salvar dados automaticamente em JSON;
* Carregar dados ao iniciar o programa.

## Tecnologias utilizadas

* Python
* JSON
* Git
* GitHub

## Estrutura do projeto

```
Gerenciador-de-Financas/
│
├── main.py          → menu e controle principal da aplicação.
├── transacoes.py    → funções relacionadas ao gerenciamento das transações.
├── dados.json       → armazenamento local dos dados.
├── README.md        → documentação do projeto.
└── .gitignore       → arquivos ignorados pelo Git.
```

## Como executar

1. Clone este repositório:

```bash
git clone https://github.com/lucasebrandao/Gerenciador-de-Financas
```

2. Acesse a pasta do projeto:

```bash
cd Gerenciador-de-Financas
```

3. Execute a aplicação:

```bash
python main.py
```

Utilize o menu para interagir com o gerenciador de finanças.