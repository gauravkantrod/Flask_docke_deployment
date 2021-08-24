"""Flask has a config attribute by default,
it’s a dictionary that you can access and set the configuration
to the “flask environment"""
from flask import Flask
from dotenv import load_dotenv, find_dotenv
from view.order_management.order import order_manager_blueprint
from view.course.course import course_blueprint
from view.basicWorking.basicCheck import basic

from flask_mysqldb import MySQL

app = Flask(__name__)

app.config['MYSQL_HOST'] = 'localhost'
app.config['MYSQL_USER'] = 'root'
app.config['MYSQL_PASSWORD'] = '12345678'
app.config['MYSQL_DB'] = 'coaching'
app.config['MYSQL_PORT'] = 3306

mysql = MySQL(app)

load_dotenv(dotenv_path='dev.env')
#environment_configuration = os.getenv('CONFIGURATION_SETUP')
#app.config.from_object(environment_configuration)

app.register_blueprint(order_manager_blueprint)
app.register_blueprint(course_blueprint)
app.register_blueprint(basic)
