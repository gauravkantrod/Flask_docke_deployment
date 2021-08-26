from flask import Blueprint, jsonify, request
import socket
from flask_mysqldb import MySQL
from mysql.connector import errorcode
import logging

logger = logging.getLogger(__name__)

course_blueprint = Blueprint('course', __name__, url_prefix='/course')


@course_blueprint.route('/', methods=['GET'])
def getCourses():
    query = "select * from course"
    try:
        connection = MySQL()
        logger.info("getCourses: Fetching all courses started!!")
        cursor = connection.connection.cursor()

        cursor.execute(query)
        records = cursor.fetchall()
        cursor.connection.commit()

        logger.info("getCourses: Fetching all courses completed!!")
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


@course_blueprint.route('/addCourse', methods=['POST'])
def addCourse():
    query = "INSERT INTO course(name, duration) values (%s, %s)"
    try:
        logger.info("addCourse: Adding course data!")
        request_data = request.get_json()
        args = (request_data['name'], request_data['duration'])

        connection = MySQL()
        cursor = connection.connection.cursor()
        cursor.execute(query, args)
        cursor.connection.commit()

        return {'code': 200}

    except connection.connector.Error as err:
        if err.errno == errorcode.ER_ACCESS_DENIED_ERROR:
            logger.error("Something is wrong with your user name or password")
        elif err.errno == errorcode.ER_BAD_DB_ERROR:
            logger.error("Database does not exist")
        else:
            logger.error(err)
    finally:
        cursor.close()


@course_blueprint.route('/deleteCourse', methods=['DELETE'])
def deleteCourse():
    return f"In delete course {socket.gethostname()}"
