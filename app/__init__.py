from flask import Flask
from models import db

from app.CustomJSONEncoder import CustomJSONEncoder
from routes import index


def create_app():
    app = Flask(__name__)
    app.json_encoder = CustomJSONEncoder

    app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://ucenter:ucenter@localhost/ucenter'
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

    app.register_blueprint(index.bp)
    db.init_app(app)

    return app
