from datetime import datetime, date, timedelta
from flask import (
    Blueprint,
    request,
    redirect,
    url_for,
    render_template
)

from app.models import Vendas
from app.utils import converte_moeda

dh = Blueprint("dh", __name__, url_prefix="/dashboard")

@dh.get("/")
def index():
    hoje = date.today()

    class dados:
        vendas = Vendas.select().where(
            Vendas.criado_em.between(
                datetime.combine(hoje, datetime.min.time()),
                datetime.combine(hoje, datetime.max.time())
            )
        )
        
        saldo  = converte_moeda(
            sum([v.total for v in vendas])
        )
        data   = datetime.now().strftime("%d/%m/%Y")
        for venda in vendas:
            venda.criado_em = venda.criado_em.strftime("%d/%m/%Y %H:%M")
            venda.total = converte_moeda(venda.total)

    return render_template("dashboard.html", dados=dados)


