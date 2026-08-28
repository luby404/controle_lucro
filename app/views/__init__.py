from flask import Flask

from .dashboard import dh
from .produtos import produtos
from .relatorios import relatorio
from .vendas import vendas


routes = [
    dh,
    produtos,
    relatorio,
    vendas,
]

def init_routes(app:Flask):

    for route in routes: app.register_blueprint(route)

    return app