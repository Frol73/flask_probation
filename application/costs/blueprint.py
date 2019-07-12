from flask import (
    Blueprint,
    render_template,
)

from application.models import Data

costs = Blueprint('costs', __name__, template_folder='templates')


@costs.route('/')
def index():
    costs = Data.query.all() # Получение в переменную списка записей трат
    return render_template('costs/index.html', costs=costs)


@costs.route('/<slug>')
def cost_detail(slug):
    cost = Data.query.filter(Data.slug == slug).first()
    return render_template('costs/cost_detail.html', cost=cost)
