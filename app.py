"""Flask has a config attribute by default,
it’s a dictionary that you can access and set the configuration
to the “flask environment"""
from flask import Flask, jsonify
import os
from dotenv import load_dotenv
from view.order_management.order import order_manager_blueprint
from view.course.course import course_blueprint
from view.basicWorking.basicCheck import basic
from view.user.user import userBlueprintObject
from flask_mysqldb import MySQL
from healthcheck import HealthCheck
import logging

app = Flask(__name__)
load_dotenv('dev.env')

logging.basicConfig(filename=os.getenv('LOGFILE_PATH'),
                    level=os.getenv('LOGGING_LEVEL'),
                    format='%(asctime)s %(levelname)s %(name)s %(threadName)s : %(message)s')

app.config['MYSQL_USER'] = os.getenv('MYSQL_USER')
app.config['MYSQL_PASSWORD'] = os.environ['MYSQL_PASSWORD']
app.config['MYSQL_HOST'] = os.environ['MYSQL_HOST']
app.config['MYSQL_DB'] = os.environ['MYSQL_DB']
app.config['MYSQL_PORT'] = int(os.environ['MYSQL_PORT'])

mysql = MySQL(app)

app.register_blueprint(order_manager_blueprint)
app.register_blueprint(course_blueprint)
app.register_blueprint(basic)
app.register_blueprint(userBlueprintObject)

health = HealthCheck()


def isAppWorking():
    return True, 'Yes Application is working!!!'


health.add_check(isAppWorking)

app.add_url_rule("/healthCheck", 'healthCheck', view_func=lambda: health.run())


@app.errorhandler(404)
def resource_not_found(e):
    return jsonify(error=str(e)), 404
