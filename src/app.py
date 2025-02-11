from flask import Flask, render_template
from database.db_postgresql import db
from models.user import User
from models.document import Document
#from src.routes import main
from config import Config

app = Flask(__name__)
app.config.from_object(Config)
db.init_app(app)  

with app.app_context():
    db.create_all()

if __name__ == "__main__":
    app.run(host="127.0.0.1", port=5000, debug=True)






