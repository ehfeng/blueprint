from flask import Flask
from flask_sqlalchemy import SQLAlchemy

from blueprint.utils import make_celery


app = Flask(__name__)
app.config.update(
    CELERY_BROKER_URL='redis://localhost:6379',
    CELERY_RESULT_BACKEND='redis://localhost:6379',
    SQLALCHEMY_DATABASE_URI='sqlite:////tmp/test.db',
    SQLALCHEMY_TRACK_MODIFICATIONS=False,
)


celery = make_celery(app)
db = SQLAlchemy(app)

from blueprint import views
