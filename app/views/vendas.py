from flask import (
    Blueprint,
    request,
    redirect,
    url_for,
    render_template,
    session
)

from app.models import (
    Usuario,
    Produtos,
    Vendas
)

vendas = Blueprint("vendas", __name__, url_prefix="/vendas")

@vendas.get("/")
def index():

    id_produto = request.args.get("edite", -1)

    class dados:
        produtos:Produtos = Produtos.select()
        carrinho:dict = session.get("carrinho", {})
        produtos_carrinho = len(carrinho)
        total_carrinho = sum([ (float(p["preco"]) * int(p["qtd"])) for i, p in carrinho.items()])

        produto = carrinho.get(id_produto)
        id = int(id_produto)

    return render_template("vendas.html", dados=dados)

@vendas.post("/new")
def new_venda():

    carrinho = session.get("carrinho", {})

    produto:Produtos = Produtos.get_or_none(Produtos.codigo == request.form.get("code", None))
    if not produto:
        produto:Produtos = Produtos.get_or_none(Produtos.id == request.form.get("produto", None))

    try:
        qtd = int(request.form.get("qtd", 1))
    except:
        qtd = 1

    
    if produto:
        carrinho[str(produto.id)] = dict(
            produto=produto.nome,
            preco=float(produto.preco_venda),
            qtd=qtd,
            subtotal=float(float(produto.preco_venda) * qtd)
        )


    session["carrinho"] = carrinho
    return redirect(url_for("vendas.index"))

@vendas.post("/update/<id>")
def update_venda(id):

    try:
        qtd = int(request.form.get("qtd", 1))
    except:
        qtd = 1

    carrinho:dict = session.get("carrinho", {})
    produto = carrinho.get(id, None)
    if produto:
        produto["subtotal"] = produto["preco"] * qtd
        produto["qtd"] = qtd

    session["carrinho"] = carrinho
    return redirect(url_for("vendas.index"))

@vendas.get("/delete/<id>")
def remove_iten(id):
    carrinho = session.get("carrinho", {})

    try:
        del carrinho[id]
    except:
        pass
    
    session["carrinho"] = carrinho
    return redirect(url_for("vendas.index"))

@vendas.get("/cancelar")
def cancelar():
    session["carrinho"] = {}
    return redirect(url_for("vendas.index"))

@vendas.get("/finalizar")
def finalizar():
    carrinho = session.get("carrinho", {})

    for id, p in carrinho.items():
        produto:Produtos = Produtos.get_or_none(Produtos.id == id)
        if produto:
            qtd      = int(p["qtd"])
            total    = produto.preco_venda * qtd
            lucro    = produto.preco_venda - produto.preco_compra


            Vendas.create(
                produto=produto,
                nome_produto=produto.nome,
                qtd=qtd,
                lucro=lucro * qtd,
                total=total,
                usuario=None
            )

    session["carrinho"] = {}
    return redirect(url_for("vendas.index"))
