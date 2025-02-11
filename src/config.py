import os

class Config:
    SQLALCHEMY_DATABASE_URI = os.getenv("DATABASE_URL")
    SQLALCHEMY_TRACK_MODIFICATIONS = False  # Desactiva warnings innecesarios

    DEBUG = os.getenv("FLASK_DEBUG", "False").lower() == "true"
    /home/emiliano/Desktop/Netlabs Academy/Sprint 5 (Custom)/Project/Sprint-5-Custom-/src

