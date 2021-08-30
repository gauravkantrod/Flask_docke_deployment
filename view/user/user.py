from flask import Blueprint, request
from schema.user import UserSchema
import logging
from database.database import db_session
from models.user import User
from werkzeug.security import generate_password_hash
from sqlalchemy import exc
from flask_jwt_extended import jwt_required, get_jwt_identity

# User's Blueprint object
userBlueprintObject = Blueprint('user', __name__, url_prefix='/api/v1/users')

logger = logging.getLogger(__name__)


@userBlueprintObject.route('/', methods=['GET'])
@jwt_required()
def getAllUsers():
    try:
        logger.info("user : getAllUsers: Fetching all users started!!")
        users = User.query.all()
        user_schema = UserSchema()
        logger.info("getAllUsers: Fetching all users completed!!")
        return {"users": user_schema.dump(users, many=True)}
    except exc.DatabaseError:
        logger.error("user : getAllUsers: DB Error occurred!!")
        db_session.rollback()
        return {"status_code": 500, 'message': "DB error occurred. Internal Server Error"}, 500
    except Exception:
        logger.error("user : getAllUsers: Error occurred!!")
        db_session.rollback()
        return {"status_code": 500, 'message': "Internal Server Error"}, 500


@userBlueprintObject.route('/getSingleUser', methods=['GET'])
def getSingleUser():
    try:
        user_email = request.args.get('user_email')
        if not user_email:
            logger.error(f"user : getSingleUser : Email not found in arguments")
            return {'status_code': 400, "message": "Email not found in arguments"}, 400
        logger.info(f"user : getSingleUser: Fetching user {user_email} data started!!")
        user = User.query.filter(User.email == user_email).one_or_none()
        user_schema = UserSchema()
        logger.info(f"user : getSingleUser: Fetching user {user_email} data completed!!")
        return {"user": user_schema.dump(user)}
    except exc:
        logger.error("user : getSingleUser: DB Error occurred!!")
        db_session.rollback()
        return {"status_code": 500, 'message': "Internal Server Error"}, 500


@userBlueprintObject.route('/addUser', methods=['POST'])
def addUser():
    try:
        logger.info("user : addUser: Adding user started!!")
        body = request.get_json()
        u = User(body['email'], generate_password_hash(body['password']), body['firstname'], body['lastname'],
                 body['isStudent'])
        db_session.add(u)
        db_session.commit()

        logger.info("user: addUser : Adding new user completed!!")
        return {"status_code": 201, 'message': f"User {body['email']} created!!"}, 201
    except exc.IntegrityError:
        logger.error(f"user : addUser : {body['email']} User already exists!!")
        db_session.rollback()
        return {"status_code": 409, 'message': f"User '{body['email']}' already exists!!"}, 409
    except exc:
        logger.error("user : addUser: DB Error occurred!!")
        db_session.rollback()
        return {"status_code": 500, 'message': "Internal Server Error"}, 500
