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

        return redirect(url_for("auth.Home"))  

    return redirect(url_for("auth.Home"))  

@auth_bp.route('/signup', methods=["GET", "POST"])
def SignUp(): 
    if request.method == "POST":
        nombre = request.form["nombre"]
        email = request.form["email"]
        clave = request.form["clave"]

        if get_user_by_email(email):
            return render_template("signup.html")

        aus.SignUp(nombre, email, clave)

        session["user_id"] = get_user_by_email(email).user_id
        return redirect(url_for("user.menu"))

    return render_template("signup.html")

@auth_bp.route('/logout')
def LogOut():
    aus.logout_user()
    return render_template("index.html") 


