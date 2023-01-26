from flask_sqlalchemy import SQLAlchemy
from flask_marshmallow import Marshmallow
from flask_migrate import Migrate
from datetime import datetime


db = SQLAlchemy()
ma = Marshmallow()


def configure(app):
    db.init_app(app)
    ma.init_app(app)
    app.db = db
    Migrate(app, app.db)


class Log(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    user_ip = db.Column(db.String(256), unique=False, nullable=False)
    searched_state = db.Column(db.String(256), unique=False, nullable=False)
    date_access = db.Column(db.DateTime, unique=False,
                            nullable=False,  default=datetime.utcnow)
