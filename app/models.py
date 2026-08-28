import peewee as orm


db = orm.SqliteDatabase("banco.db")

class Model(orm.Model):
    class Meta:
        database = db


class Usuario(Model):

    class Rule:
        admin    = "admin"
        vendedor = "vendedor"

    username = orm.CharField(max_length=256, unique=True)
    password = orm.CharField(max_length=256)
    role     = orm.CharField(max_length=100, default=Rule.vendedor)

class Produtos(Model):
    nome   = orm.CharField(max_length=256, unique=True)
    codigo = orm.CharField(max_length=256, null=True)

    preco_compra = orm.DecimalField(decimal_places=2, max_digits=16)
    preco_venda  = orm.DecimalField(decimal_places=2, max_digits=16)

    estoque = orm.IntegerField(default=0)

class Vendas(Model):
    produto = orm.ForeignKeyField(Produtos, backref="vendas")
    usuario = orm.ForeignKeyField(Usuario, backref="vendas", null=True)

    nome_produto = orm.CharField(max_length=256)
    qtd      = orm.IntegerField()

    subtotal = orm.DecimalField(decimal_places=2, max_digits=16)
    lucro    = orm.DecimalField(decimal_places=2, max_digits=16)
    total    = orm.DecimalField(decimal_places=2, max_digits=16)


def init_db():
    db.connect()
    db.create_tables([Usuario, Produtos, Vendas])


