from flask import Blueprint, jsonify
import socket
from flask_mysqldb import MySQL

course_blueprint = Blueprint('course', __name__, url_prefix='/course')
mysql = MySQL()

@course_blueprint.route('/', methods=['GET'])
def getCourses():
    connection = mysql.connection.cursor()
    query = "select * from course"
    connection.execute(query)
    records = connection.fetchall()
    mysql.connection.commit()
    connection.close()

    return jsonify(records)


@course_blueprint.route('/addCourse', methods=['POST'])
def addCourse():
    return f"In add course Container ID is {socket.gethostname()}!!!"


@course_blueprint.route('/deleteCourse', methods=['DELETE'])
def deleteCourse():
    return f"In delete course {socket.gethostname()}"
