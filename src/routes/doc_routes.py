from flask import Blueprint, request, jsonify, session, render_template
from services.doc_service import get_docs_for_collab

document_bp = Blueprint('document', __name__)

@document_bp.route('/documents')
def get_documents():
    docs = get_docs_for_collab(session['user_id'])
    return render_template('docs.html', documents=docs)

@document_bp.route('/create')
def create_doc():
    
    return 
