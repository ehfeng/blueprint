from blueprint import app
from blueprint.tasks import create_user


@app.route('/')
def index():
    create_user.delay()
    return 'Hello, blueprint!'
