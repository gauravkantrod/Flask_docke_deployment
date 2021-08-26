from flask import Blueprint, jsonify, request
from flask_mysqldb import MySQL
from mysql.connector import errorcode
import logging

# User's Blueprint object
userBlueprintObject = Blueprint('user', __name__, url_prefix='/users')

logger = logging.getLogger(__name__)


@userBlueprintObject.route('/', methods=['GET'])
def getAllUsers():
    query = 'SELECT * FROM USERS'
    try:
        logger.info("getAllUsers: Fetching all users started")
        connection = MySQL()
        cursor = connection.connection.cursor()
        cursor.execute(query)
        records = cursor.fetchall()
        cursor.connection.commit()

        logger.info("getCourses: Fetching all users completed!!")
        return jsonify(records)
    except connection.connector.Error as err:
        if err.errno == errorcode.ER_ACCESS_DENIED_ERROR:
            logger.error("Something is wrong with your user name or password")
        elif err.errno == errorcode.ER_BAD_DB_ERROR:
            logger.error("Database does not exist")
        else:
            logger.error(err)
    finally:
        cursor.close()


@userBlueprintObject.route('/addUser', methods=['POST'])
def addUser():
    query = 'INSERT INTO users(firstname, lastname, email, isStudent) values (%s, %s, %s, %s)'
    try:
        logger.info("addUser: Adding user!!")
        data = request.get_json()
        args = (data['firstname'], data['lastname'], data['email'], data['isStudent'])
        connection = MySQL()
        cursor = connection.connection.cursor()
        cursor.execute(query, args)
        cursor.connection.commit()

        return {"code": 200, "message": "User added!!"}
    except connection.connector.Error as err:
        if err.errno == errorcode.ER_ACCESS_DENIED_ERROR:
            logger.error("Something is wrong with your user name or password")
        elif err.errno == errorcode.ER_BAD_DB_ERROR:
            logger.error("Database does not exist")
        else:
            logger.error(err)
    finally:
        cursor.close()
