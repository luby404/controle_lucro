from flask import Flask

from .views import init_routes
from .models import init_db


app = Flask(__name__)
app.secret_key = "soasdasdasdkjnas das dkansdansld asd as daj"

init_db()
init_routes(app)


