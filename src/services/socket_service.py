from flask_socketio import SocketIO

socketio = SocketIO()

def init_sockets(app):
    socketio.init_app(app)
