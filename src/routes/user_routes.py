from flask import Blueprint, render_template, session
from services.doc_service import get_docs_by_creator, get_docs_collab

user_bp = Blueprint('user', __name__)

@user_bp.route('/menu')
def menu():
    documents = get_docs_by_creator(session['user_id'])
    documents_collab = get_docs_collab(session['user_id'])
    return render_template('menu.html', documents=documents, dc=documents_collab)