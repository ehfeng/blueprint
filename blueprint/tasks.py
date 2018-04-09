from blueprint import celery, db
from blueprint.models import User

@celery.task()
def add_together(a, b):
    user = User()
    db.session.add(user)
    db.session.commit()
    print('Hello, Celery!')
