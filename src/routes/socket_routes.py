from flask import Blueprint
from flask_socketio import emit, join_room
from database.db_postgresql import db
from models.document import Document
from services.socket_service import socketio 
from services.doc_service import update_doc

socket_bp = Blueprint("socket_routes", __name__)

@socketio.on('join_document')
def join_document(data):
    room = f"document_{data['doc_id']}"
    join_room(room)
    print(f"Usuario se unió al documento {data['doc_id']}")

@socketio.on('edit_document')
def edit_document(data):
    doc_id = data['doc_id']
    title = data.get('title', '') 
    content = data['content']

   
    success = update_doc(doc_id, title, content)

    if success:
        room = f"document_{doc_id}"
        emit('update_document', {'title': title, 'content': content}, room=room, include_self=False)

@socketio.on('connect')
def handle_connect():
    print("Cliente conectado")

@socketio.on('disconnect')
def handle_disconnect():
    print("Cliente desconectado")
