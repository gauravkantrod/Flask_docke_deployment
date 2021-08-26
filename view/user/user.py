from flask import Blueprint, jsonify, request
from flask_mysqldb import MySQL
from mysql.connector import errorcode
import logging

# user Blueprint object
user = Blueprint('user', __name__, url_prefix='/users')

logger = logging.getLogger(__name__)


@user.route('/', methods=['GET'])
def getAllUsers():
    query = 'SELECT * FROM USERS'
    try:
        logger.info("getAllUsers: Featching all users")
        connection = MySQL()
        cursor = connection.connection.cursor()
        cursor.execute(query)
        records = cursor.fetchall()
        cursor.connection.commit()

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
