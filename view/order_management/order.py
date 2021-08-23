from flask import Blueprint
import socket

order_manager_blueprint = Blueprint('order_manager_blueprint', __name__, url_prefix="/order")


@order_manager_blueprint.route('/myorders')
def myorders():
    return f"These are your orders. -- {socket.gethostname()}"


@order_manager_blueprint.route('/placeorder')
def placeorder():
    return "Placing order"


@order_manager_blueprint.route('/cancelorder')
def cancelorder():
    return "Cancelling order"
