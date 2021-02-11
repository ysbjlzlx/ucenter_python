from flask import Blueprint, jsonify

from models import db
from models.User import User

bp = Blueprint("index", __name__)


@bp.route('/')
def index():
    user = User(username="ccc")
    user.password = "cc"
    db.session.add(user)
    db.session.commit()
    users = User.query.all()
    return jsonify(users)
