from blueprint import celery, db
from blueprint.models import User
from blueprint.web.models import Post

@celery.task()
def create_user():
    print('Hello, Celery!')
    user = User()
    db.session.add(user)
    post = Post()
    db.session.add(post)
    db.session.commit()
