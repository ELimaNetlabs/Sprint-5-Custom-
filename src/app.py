from flask import Flask, render_template
from database.db_postgresql import db
from models.user import User
from models.document import Document
from routes.doc_routes import document_bp
from routes.user_routes import user_bp
from routes.auth_routes import auth_bp
from config import Config
from flask_socketio import SocketIO, emit, join_room, leave_room


app = Flask(__name__)
app.config.from_object(Config)
db.init_app(app)  
app.secret_key = "mi_clave_super_secreta_123"
socketio = SocketIO(app)

app.register_blueprint(document_bp)
app.register_blueprint(user_bp)
app.register_blueprint(auth_bp)

@socketio.on('connect')
def handle_connect():
    print("Cliente conectado")

@socketio.on('join_document')
def join_document(data):
    room = f"document_{data['doc_id']}"
    join_room(room)
    print(f"Usuario se unió al documento {data['doc_id']}")

@socketio.on('edit_document')
def edit_document(data):
    room = f"document_{data['doc_id']}"
    content = data['content']

    doc = Document.query.get(data['doc_id'])
    if doc:
        doc.content = content
        db.session.commit()

    emit('update_document', {'content': content}, room=room, include_self=False)

@socketio.on('disconnect')
def handle_disconnect():
    print("Cliente desconectado")


with app.app_context():
    db.create_all()

if __name__ == "__main__":
    socketio.run(app, host="192.168.100.154", port=5000, debug=True)







