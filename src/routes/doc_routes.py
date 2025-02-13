from flask import Blueprint, request, jsonify

document_bp = Blueprint('document', __name__)

@document_bp.route('/documents')
def get_documents():
    return jsonify({"message": "Lista de documentos"})

@document_bp.route('/documents/<int:doc_id>')
def update_document(doc_id):
    data = request.json
    return jsonify({"message": f"Documento {doc_id} actualizado"})
