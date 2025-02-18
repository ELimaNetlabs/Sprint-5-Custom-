from flask import Flask, render_template
from database.db_postgresql import db
from models.user import User
from models.document import Document
from routes.doc_routes import document_bp
from routes.user_routes import user_bp
from routes.auth_routes import auth_bp
from config import Config

app = Flask(__name__)
app.config.from_object(Config)
db.init_app(app)  
app.secret_key = "mi_clave_super_secreta_123"


app.register_blueprint(document_bp)
app.register_blueprint(user_bp)
app.register_blueprint(auth_bp)

with app.app_context():
    db.create_all()

if __name__ == "__main__":
    app.run(host="192.168.100.153", port=5000, debug=True)






