from database.db_postgresql import db
from models.user import User  
from datetime import datetime

def get_all_users():
    return User.query.all()

def get_user_by_id(user_id):
    user = User.query.get(user_id)
    if user:
        print(user.to_dict())


def get_user_by_email(email):
    user = User.query.filter_by(email=email).first()
    if user:
        return user


def create_user(name, email, password, date):
    new_user = User(
        nombre=name,
        clave=password,
        email=email,
        fecha_nacimiento=datetime.strptime(date, "%Y-%m-%d")
    )

    db.session.add(new_user)
    db.session.commit()  # Guarda en la base de datos

    return new_user

