from database.db_postgresql import db

class User(db.Model):
    __tablename__ = "users"  

    user_id = db.Column(db.String, primary_key=True)
    nombre = db.Column(db.String, nullable=False)
    clave = db.Column(db.String, nullable=False)
    email = db.Column(db.String, unique=True, nullable=False)
    fecha_nacimiento = db.Column(db.Date, nullable=False)

    def __init__(self, user_id, nombre, clave, email, fecha_nacimiento):
        self.user_id = user_id
        self.nombre = nombre
        self.clave = clave
        self.email = email
        self.fecha_nacimiento = fecha_nacimiento

    def to_dict(self):
        return {
            "user_id": self.user_id,
            "nombre": self.nombre,
            "email": self.email,
            "fecha_nacimiento": self.fecha_nacimiento.strftime("%Y-%m-%d")  
        }
