from flask import Blueprint, render_template

user_bp = Blueprint('user', __name__)

@user_bp.route('/menu')
def menu():
    return render_template("menu.html")