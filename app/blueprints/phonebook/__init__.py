from flask import Blueprint

phonebook = Blueprint('commerce', __name__, url_prefix='/cm')


from . import routes, models