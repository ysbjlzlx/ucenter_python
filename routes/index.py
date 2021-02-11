from flask import Blueprint, jsonify

from models import db
from models.User import User

bp = Blueprint("index", __name__)


@bp.route('/')
def index():
    db.session.add(User(username="ccc", password="ccc"))
    db.session.commit()
    users = User.query.all()
    return jsonify(users)
