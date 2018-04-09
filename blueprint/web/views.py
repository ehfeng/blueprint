from flask import Blueprint

from blueprint.web.tasks import create_user


web = Blueprint('web', __name__)


@web.route('/')
def index():
    create_user.delay()
    return 'Hello, blueprint!'
