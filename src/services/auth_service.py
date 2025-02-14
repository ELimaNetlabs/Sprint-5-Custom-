from flask import session
from database.db_postgresql import db
from services import user_service as us

def SignUp(name, email, password, date):
    us.create_user(name, email, password, date)

def SignIn(email, password):
    user = us.get_user_by_email(email)
    if user.clave == password:
        return True
    return False

def logout_user():
    session.pop("user_id", None)
