

from src.models.user import User
import src.middleware.auth as auth

def sign_in(username, pwd):
    """
       Login
    """

    try:
        result = fetch_user(username, pwd)

        if result:
            auth.user = result
            return dict(status= 200, body= auth.user, message= "Login bem sucedido!")

    except Exception as e:
        return dict(status= 422, body= e)

def sign_out():
    """
       Logout
    """
    auth.user = None

def sign_up(usr, pwd):
    """
       Registro
    """
    user = User(username= usr, password = pwd)

    if user.save():
        auth.user = user

        return dict(status=201, body=auth.user, message="Usuario Registrado!")
    else:
        return dict(status=422, body=user)

def fetch_user(username, password) -> object:
    """
    Busca pelo usuario e retorna-o
    :rtype: object
    :returns: User
    """
    return User.select().where(User.username == username and User.password == password).get()