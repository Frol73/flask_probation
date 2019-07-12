from application.app import app
from application import view
from application.app import db
from application.costs.blueprint import costs


app.register_blueprint(costs, url_prefix='/costs')


if __name__ == '__main__':
    app.run()
