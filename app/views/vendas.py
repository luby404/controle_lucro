from flask import (
    Blueprint,
    request,
    redirect,
    url_for,
    render_template
)

vendas = Blueprint("vendas", __name__, url_prefix="/vendas")

@vendas.get("/")
def index():
    return render_template("vendas.html")


