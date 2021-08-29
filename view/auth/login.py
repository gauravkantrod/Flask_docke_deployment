from flask import Blueprint, request
from schema.user import UserSchema
import logging
from database.database import db_session
from models.user import User
from werkzeug.security import check_password_hash, generate_password_hash
from sqlalchemy import exc

# login Blueprint object
loginBlueprintObject = Blueprint('login', __name__, url_prefix='/api/v1/login')


@loginBlueprintObject.route('/', methods=['GET'])
def userLogin():
    body = request.get_json()
    user = User.query.filter(User.email == body['email']).one_or_none()

    if user:
        if check_password_hash(user.password, body['password']):
            logging.info(f"login : User {body['email']} authenticated!!")
            return {'status_code': 200, "message": "User authenticated!!"}, 200
        else:
            logging.error(f"login : User {body['email']} not authenticated. Password is wrong!!")
            return {'status_code': 401, "message": "Username/email or password is not correct!!"}, 401
    else:
        logging.error(f"login : User {body['email']} not authenticated. Email and password both are wrong!!")
        return {'status_code': 404, "message": "Username/email or password is not correct!!"}, 404
