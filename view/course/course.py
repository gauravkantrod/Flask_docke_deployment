from flask import Blueprint, jsonify
import socket
from flask_mysqldb import MySQL
from mysql.connector import errorcode
import logging

logger = logging.getLogger(__name__)

course_blueprint = Blueprint('course', __name__, url_prefix='/course')
mysql = MySQL()


@course_blueprint.route('/', methods=['GET'])
def getCourses():
    try:
        logger.info("In: getCourses")
        connection = mysql.connection.cursor()
        query = "select * from course"
        connection.execute(query)
        records = connection.fetchall()
        mysql.connection.commit()
        connection.close()

        return jsonify(records)
    except mysql.connector.Error as err:
        if err.errno == errorcode.ER_ACCESS_DENIED_ERROR:
            logger.error("Something is wrong with your user name or password")
        elif err.errno == errorcode.ER_BAD_DB_ERROR:
            logger.error("Database does not exist")
        else:
            logger.error(err)
    else:
        print("")


@course_blueprint.route('/addCourse', methods=['POST'])
def addCourse():
    return f"In add course Container ID is {socket.gethostname()}!!!"


@course_blueprint.route('/deleteCourse', methods=['DELETE'])
def deleteCourse():
    return f"In delete course {socket.gethostname()}"
