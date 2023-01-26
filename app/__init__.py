from flask import Flask
from environs import Env

from app.views.logs import bp_logs

from app.models import configure


def create_app():
    env = Env()
    env.read_env()

    app = Flask(__name__)

    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
    app.config['SQLALCHEMY_DATABASE_URI'] = env.str("SQLALCHEMY_DATABASE_URI")

    configure(app)

    app.register_blueprint(bp_logs)

    return app
