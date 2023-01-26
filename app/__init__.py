from flask import Flask
from environs import Env
# from flask_restplus import Api
import yaml

from app.views.logs import bp_logs

from app.models import configure


def create_app():
    env = Env()
    env.read_env()

    app = Flask(__name__)

    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
    app.config['SQLALCHEMY_DATABASE_URI'] = env.str("SQLALCHEMY_DATABASE_URI")

    configure(app)

    # api = Api(app)

    # with open("uf_consult.yaml") as file:
    #     documentation = yaml.load(file, Loader=yaml.FullLoader)
    # api.add_documentation(documentation)

    # api.swaggerui_blueprint.add_resource(
    #     '/apidocs/swagger.json', '/swagger.json')

    # app.register_blueprint(api.swaggerui_blueprint, url_prefix='/apidocs')
    app.register_blueprint(bp_logs)

    return app
