from flask import Blueprint, render_template, session, redirect, url_for, request
from services import auth_service as aus
from services.user_service import get_user_by_email

auth_bp = Blueprint('auth', __name__)

@auth_bp.route('/')
def Home():
    if "user_id" in session:
        return redirect(url_for("user.menu"))   
    return render_template("index.html")  

@auth_bp.route('/signin', methods=["GET", "POST"])
def SignIn():
    if request.method == "POST":
        email = request.form["email"]
        clave = request.form["clave"]

        if aus.SignIn(email, clave): 
            session["user_id"] = get_user_by_email(email).user_id
            return redirect(url_for("user.menu"))  

        return render_template("signin.html")

    return render_template("signin.html")

@auth_bp.route('/signup', methods=["GET", "POST"])
def SignUp(): 
    if request.method == "POST":
        nombre = request.form["nombre"]
        email = request.form["email"]
        clave = request.form["clave"]
        fecha_nacimiento = request.form["fecha_nacimiento"]

        # Verificar si el usuario ya existe
        if get_user_by_email(email):
            return render_template("signup.html")

        # Crear nuevo usuario
        aus.SignUp(nombre, email, clave, fecha_nacimiento)

        # Guardar usuario en sesión y redirigir al menú
        session["user_id"] = get_user_by_email(email).user_id
        return redirect(url_for("user.menu"))

    return render_template("signup.html")


