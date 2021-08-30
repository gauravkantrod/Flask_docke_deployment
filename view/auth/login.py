from flask import Blueprint, request
import logging
from models.user import User
from werkzeug.security import check_password_hash
from flask_jwt_extended import create_access_token

# login Blueprint object
loginBlueprintObject = Blueprint('login', __name__, url_prefix='/api/v1/login')


@loginBlueprintObject.route('/', methods=['GET'])
def userLogin():
    body = request.get_json()
    user = User.query.filter(User.email == body['email']).one_or_none()

    if user:
        if check_password_hash(user.password, body['password']):
            logging.info(f"login : User {body['email']} authenticated!!")
            # create a new token with the user id inside
            access_token = create_access_token(identity=user.email)
            return {'status_code': 200, "message": "User authenticated!!", "token": access_token}, 200
        else:
            logging.error(f"login : User {body['email']} not authenticated. Password is wrong!!")
            return {'status_code': 401, "message": "Username/email or password is not correct!!"}, 401
    else:
        logging.error(f"login : User {body['email']} not authenticated. Email and password both are wrong!!")
        return {'status_code': 404, "message": "Username/email or password is not correct!!"}, 404
