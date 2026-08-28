from flask import (
    Blueprint,
    request,
    redirect,
    url_for,
    render_template,
    flash
)

from app.models import Produtos

produtos = Blueprint("produtos", __name__, url_prefix="/produto")

@produtos.get("/")
def index():

    
    
    produtos = Produtos.select()
    for produto in produtos:
        produto.lucro = produto.preco_venda - produto.preco_compra

    edite   = request.args.get("edite", False)
    produto = Produtos.get_or_none(Produtos.id == edite)

    return render_template("produtos.html", produtos=produtos, produto=produto)

@produtos.post("/create")
def new_produto():

    nome   = request.form.get("nome")
    compra = request.form.get("compra")
    venda  = request.form.get("venda")

    try:
        Produtos.create(
            nome=nome,
            preco_compra=compra,
            preco_venda=venda
        )
    except:
        flash("Não foi possivel cadastrar o produto")

    return redirect(url_for("produtos.index"))

@produtos.post("/update/<id>")
def update_produto(id):
    produto:Produtos = Produtos.get_or_none(Produtos.id == id)
    nome   = request.form.get("nome")
    compra = request.form.get("compra")
    venda  = request.form.get("venda")

    if produto:
        produto.nome = nome
        produto.preco_compra = compra
        produto.preco_venda = venda
        produto.save()

    return redirect(url_for("produtos.index"))

@produtos.get("/update/<id>")
def delete_produto(id):
    produto:Produtos = Produtos.get_or_none(Produtos.id == id)
    if produto:
        Produtos.delete_instance(produto)

    return redirect(url_for("produtos.index"))


