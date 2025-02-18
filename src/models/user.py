from database.db_postgresql import db

class User(db.Model):
    __tablename__ = "users"  

    user_id = db.Column(db.Integer, primary_key=True, autoincrement=True)  
    nombre = db.Column(db.String, nullable=False)
    clave = db.Column(db.String, nullable=False)
    email = db.Column(db.String, unique=True, nullable=False)

    def __init__(self, nombre, clave, email):
        self.nombre = nombre
        self.clave = clave
        self.email = email

    def to_dict(self):
        return {
            "user_id": self.user_id,
            "nombre": self.nombre,
            "password": self.clave,
            "email": self.email 
        }

