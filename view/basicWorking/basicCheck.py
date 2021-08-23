from flask import Blueprint

basic = Blueprint('Basic_Blueprint', __name__)


@basic.route('/')
def checkApplication():
    return f"Basic Application is Working!!"
