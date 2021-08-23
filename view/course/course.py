from flask import Blueprint
import os
import socket

course_blueprint = Blueprint('course', __name__, url_prefix='/course')


@course_blueprint.route('/', methods=['GET'])
def getCourses():
    return f"Get all courses {os.getenv('SECRET_KEY')}!!"


@course_blueprint.route('/addCourse', methods=['POST'])
def addCourse():
    return f"In add course Container ID is {socket.gethostname()}!!!"


@course_blueprint.route('/deleteCourse', methods=['DELETE'])
def deleteCourse():
    return f"In delete course {socket.gethostname()}"
