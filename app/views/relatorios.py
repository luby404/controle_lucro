from flask import (
    Blueprint,
    request,
    redirect,
    url_for,
    render_template
)

relatorio = Blueprint("relatorio", __name__, url_prefix="/relatorio")

@relatorio.get("/")
def index():
    return render_template("relatorio.html")


