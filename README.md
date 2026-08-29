# Controle de Lucro

Sistema web para pequenos negócios (ex: cantinas) 
controlarem o lucro das suas vendas de forma simples: 
cadastra os produtos com preço de compra e venda, regista as vendas, 
e o sistema calcula automaticamente quanto entrou de dinheiro e quanto foi de lucro

## Funcionalidades

- **Cadastro de produtos** — nome, preço de compra, preço de venda e estoque
- **Controlo de vendas** — regista a venda de um produto, dá baixa automática no estoque
- **Cálculo automático de lucro** — lucro por produto, por venda e lucro total acumulado
- **Faturamento/Relatórios** — total de dinheiro que entrou (receita), separado do lucro

## Tecnologias

- [Python 3](https://www.python.org/) - linguagem
- [Flask](https://flask.palletsprojects.com/) — framework web
- [Peewee](http://docs.peewee-orm.com/) — ORM
- [SQLite3](https://www.sqlite.org/) — base de dados

## Requisitos

- Python 3.9 ou superior
- uv

## Estrutura do projeto

```
.
├── app
│   ├── __init__.py
│   ├── models.py
│   ├── __pycache__
│   │   ├── __init__.cpython-314.pyc
│   │   ├── models.cpython-314.pyc
│   │   └── utils.cpython-314.pyc
│   ├── static
│   │   ├── css
│   │   │   ├── base.css
│   │   │   ├── home.css
│   │   │   └── painel.css
│   │   └── js
│   ├── templates
│   │   ├── dashboard.html
│   │   ├── leyout.html
│   │   ├── login.html
│   │   ├── produtos.html
│   │   ├── relatorio.html
│   │   └── vendas.html
│   ├── utils.py
│   └── views
│       ├── dashboard.py
│       ├── __init__.py
│       ├── produtos.py
│       ├── __pycache__
│       │   ├── dashboard.cpython-314.pyc
│       │   ├── __init__.cpython-314.pyc
│       │   ├── produtos.cpython-314.pyc
│       │   ├── relatorios.cpython-314.pyc
│       │   └── vendas.cpython-314.pyc
│       ├── relatorios.py
│       └── vendas.py
├── banco.db
├── main.py
├── pyproject.toml
├── README.md
└── uv.lock
```

## Uso básico

1. Aceder ao sistema no navegador.
2. Ir a **Produtos** e cadastrar o produto com preço de compra, preço de venda e quantidade em estoque.
3. Ir a **Vendas** e registar a venda do produto — o estoque é atualizado automaticamente.
4. Consultar o **Painel** para ver o total de dinheiro que entrou (faturamento) e o lucro total acumulado.
