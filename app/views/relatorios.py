from flask import Blueprint, request, render_template
from app.utils import lucro_por_produto, mais_vendidos, resumo_periodo
from datetime import datetime, timedelta

relatorio = Blueprint("relatorio", __name__, url_prefix="/relatorio")

@relatorio.route("/", methods=["GET", "POST"])
def index():
    data_start = None
    data_end = None

    if request.method == "POST":
        data_start = request.form.get("data_start") or None
        data_end = request.form.get("data_end") or None

    lucro = lucro_por_produto(data_start, data_end)
    vendidos = mais_vendidos(data_start, data_end)
    resumo = resumo_periodo(data_start, data_end)

    return render_template(
        "relatorio.html",
        lucro=lucro,
        vendidos=vendidos,
        resumo=resumo,
        data_start=data_start,
        data_end=data_end,
    )