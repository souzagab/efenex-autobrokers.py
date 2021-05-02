from app.models.user import User

def index():
    users = User.select()
    return users