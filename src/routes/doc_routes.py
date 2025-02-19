from flask import Blueprint, request, session, render_template, redirect, url_for
from services.doc_service import get_docs_for_collab, create_doc, update_doc, get_doc_by_id, collaborate

document_bp = Blueprint('document', __name__)

@document_bp.route('/documents')
def get_documents():
    docs = get_docs_for_collab(session['user_id'])
    return render_template('docs.html', documents=docs)

@document_bp.route('/create', methods=["GET", "POST"])
def create_document():
    if request.method == "POST":
        title = request.form["title"]
        creator = session.get('user_id')
        
        new_doc = create_doc(title, creator)
        
        return render_template("editor.html", document=new_doc)
    
    return render_template("create_doc.html")

@document_bp.route('/update/<int:doc_id>', methods=["POST"])
def update_document(doc_id):
    if update_doc(doc_id, request.form.get("title"), request.form.get("content")):
        return redirect(url_for("user.menu"))
    
@document_bp.route('/editor/<int:doc_id>', methods=["GET"])
def editor(doc_id):
    document = get_doc_by_id(doc_id)
    return render_template("editor.html", document=document)

@document_bp.route('/collaborate/<int:doc_id>', methods=["GET"])
def collaborate_doc(doc_id):
    if collaborate(doc_id, session['user_id']):
        return redirect(url_for("user.menu"))
    
