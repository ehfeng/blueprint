from blueprint import celery, db
from blueprint.models import User

@celery.task()
def create_user():
    print('Hello, Celery!')
    user = User()
    db.session.add(user)
    db.session.commit()
