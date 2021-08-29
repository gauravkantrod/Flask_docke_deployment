from flask import Blueprint, jsonify, request, make_response
from schema.user import UserSchema
import logging
from database.database import db_session
from models.user import User
from werkzeug.security import check_password_hash, generate_password_hash

# User's Blueprint object
userBlueprintObject = Blueprint('user', __name__, url_prefix='/users')

logger = logging.getLogger(__name__)


@userBlueprintObject.route('/', methods=['GET'])
def getAllUsers():
    users = User.query.all()
    len(users)
    user_schema = UserSchema()
    return {"users" : user_schema.dump(users, many=True)}


@userBlueprintObject.route('/addUser', methods=['POST'])
def addUser():
    logger.info("addUser: Adding user!!")
    data = request.get_json()
    u = User(data['email'], generate_password_hash(data['password']), data['firstname'], data['lastname'], data['isStudent'])
    db_session.add(u)
    db_session.commit()

    logger.info("user: Adding new user!!")
    return {"code": 200, 'message': "New user added!!!"}
