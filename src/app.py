from flask import Flask
from database.db_postgresql import db
from routes.doc_routes import document_bp
from routes.user_routes import user_bp
from routes.auth_routes import auth_bp
from routes.socket_routes import socket_bp  
from config import Config
from services.socket_service import socketio, init_sockets 

app = Flask(__name__)
app.config.from_object(Config)
db.init_app(app)  
app.secret_key = "mi_clave_super_secreta_123"

app.register_blueprint(document_bp)
app.register_blueprint(user_bp)
app.register_blueprint(auth_bp)
app.register_blueprint(socket_bp)  

init_sockets(app)

with app.app_context():
    db.create_all()

if __name__ == "__main__":
    socketio.run(app, host="192.168.1.15", port=5000, debug=True)
