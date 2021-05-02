global user

user = None

def user_logged_in():
    return user is not None

def logout():
    user = None