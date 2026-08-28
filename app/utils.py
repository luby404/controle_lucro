from peewee import fn
from app.models import Vendas

from peewee import fn
from datetime import datetime, timedelta
from .models import Vendas

def converte_moeda(valor):
    return f"kz {valor:,.2f}"



def _parse_periodo(data_inicio=None, data_fim=None):
    """Converte strings 'yyyy-mm-dd' em datetime, cobrindo o dia inteiro."""
    if data_inicio and data_fim:
        inicio = datetime.strptime(data_inicio, "%Y-%m-%d")
        fim = datetime.strptime(data_fim, "%Y-%m-%d") + timedelta(
            hours=23, minutes=59, seconds=59
        )
        return inicio, fim
    return None, None


def resumo_periodo(data_inicio=None, data_fim=None):
    """Cards do topo: lucro, faturamento, vendas, ticket médio."""
    query = Vendas.select(
        fn.SUM(Vendas.lucro).alias("lucro"),
        fn.SUM(Vendas.total).alias("faturamento"),
        fn.SUM(Vendas.qtd).alias("vendas"),
    )

    inicio, fim = _parse_periodo(data_inicio, data_fim)
    if inicio and fim:
        query = query.where(Vendas.criado_em.between(inicio, fim))

    row = query.dicts().get()

    lucro = row["lucro"] or 0
    faturamento = row["faturamento"] or 0
    vendas = row["vendas"] or 0
    ticket_medio = (faturamento / vendas) if vendas else 0

    return {
        "lucro": lucro,
        "faturamento": faturamento,
        "vendas": vendas,
        "ticket_medio": ticket_medio,
    }


def lucro_por_produto(data_inicio=None, data_fim=None):
    query = (
        Vendas.select(
            Vendas.nome_produto,
            fn.SUM(Vendas.lucro).alias("total_lucro"),
        )
        .group_by(Vendas.nome_produto)
        .order_by(fn.SUM(Vendas.lucro).desc())
    )

    inicio, fim = _parse_periodo(data_inicio, data_fim)
    if inicio and fim:
        query = query.where(Vendas.criado_em.between(inicio, fim))

    resultados = list(query.dicts())

    if resultados:
        maior = max(r["total_lucro"] for r in resultados)
        for r in resultados:
            r["percentual"] = (float(r["total_lucro"]) / float(maior)) * 100 if maior else 0

    return resultados


def mais_vendidos(data_inicio=None, data_fim=None):
    query = (
        Vendas.select(
            Vendas.nome_produto,
            fn.SUM(Vendas.qtd).alias("total_qtd"),
        )
        .group_by(Vendas.nome_produto)
        .order_by(fn.SUM(Vendas.qtd).desc())
    )

    inicio, fim = _parse_periodo(data_inicio, data_fim)
    if inicio and fim:
        query = query.where(Vendas.criado_em.between(inicio, fim))

    resultados = list(query.dicts())

    if resultados:
        maior = max(r["total_qtd"] for r in resultados)
        for r in resultados:
            r["percentual"] = (r["total_qtd"] / maior) * 100 if maior else 0

    return resultados



