from flask import (
    Blueprint,
    request,
    redirect,
    url_for,
    render_template
)

dh = Blueprint("dh", __name__, url_prefix="/dashboard")

@dh.get("/")
def index():
    return render_template("dashboard.html")


