"""Flask has a config attribute by default,
it’s a dictionary that you can access and set the configuration
to the “flask environment"""
from flask import Flask
import os
#from dotenv import load_dotenv, find_dotenv
from view.order_management.order import order_manager_blueprint
from view.course.course import course_blueprint
from view.basicWorking.basicCheck import basic

app = Flask(__name__)
#load_dotenv(find_dotenv())

environment_configuration = os.getenv('CONFIGURATION_SETUP')
app.config.from_object(environment_configuration)

app.register_blueprint(order_manager_blueprint)
app.register_blueprint(course_blueprint)
app.register_blueprint(basic)