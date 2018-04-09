from blueprint import app
from blueprint.tasks import create_user


@app.route('/')
def index():
    add_together.delay()
    return 'Hello, Flask blueprint!'
