"""Flask has a config attribute by default,
it’s a dictionary that you can access and set the configuration
to the “flask environment"""
from flask import Flask, jsonify
from flask_jwt_extended import JWTManager
import os
from dotenv import load_dotenv
from view.order_management.order import order_manager_blueprint
from view.course.course import course_blueprint
from view.basicWorking.basicCheck import basic
from view.user.user import userBlueprintObject
from view.auth.login import loginBlueprintObject
#from flask_mysqldb import MySQL
#from flask_sqlalchemy import SQLAlchemy
from healthcheck import HealthCheck
import logging
from database.database import db_session, init_db
from datetime import timedelta

app = Flask(__name__)
load_dotenv('dev.env')
app.config.from_object(os.getenv('CONFIGURATION_SETUP'))
#init_db()


logging.basicConfig(filename=app.config['LOGFILE_PATH'],
                    level=app.config['LOGGING_LEVEL'],
                    format='%(asctime)s %(levelname)s %(name)s %(threadName)s : %(message)s')


app.config['JWT_ACCESS_TOKEN_EXPIRES'] = timedelta(seconds=app.config['JWT_ACCESS_TOKEN_EXPIRES_TIME'])
jwt = JWTManager(app)

app.register_blueprint(order_manager_blueprint)
app.register_blueprint(course_blueprint)
app.register_blueprint(basic)
app.register_blueprint(userBlueprintObject)
app.register_blueprint(loginBlueprintObject)

health = HealthCheck()


def isAppWorking():
    return True, 'Yes Application is working!!!'


health.add_check(isAppWorking)

app.add_url_rule("/api/v1/healthCheck", 'healthCheck', view_func=lambda: health.run())


@app.errorhandler(404)
def resource_not_found(e):
    return jsonify(error=str(e)), 404


@app.teardown_appcontext
def shutdown_session(exception=None):
    logging.info(f"DB connection removed!!!")
    db_session.remove()


class AppCtxConf:
    def getAppCtxConf(self):
        return app.config

