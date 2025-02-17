from database.db_postgresql import db
from models.document import Document, document_collaborators
from models.user import User  

def get_all_docs():
    return Document.query.all()

def get_doc_by_id(doc_id):
    doc = Document.query.get(doc_id)
    if doc:
        return doc

def get_docs_by_title(title):
    doc = Document.query.filter_by(title=title).first()
    if doc:
        return doc

def get_docs_by_creator(creator_id):
    return Document.query.filter_by(creator_id=creator_id).all()

def get_docs_collab(user_id):
    user = User.query.get(user_id)
    return user.documents if user else []


def get_docs_for_collab(user_id):
    # Subquery para documentos donde el usuario es creador
    created_docs = db.session.query(Document.doc_id).filter(Document.creator_id == user_id)

    # Subquery para documentos donde el usuario es colaborador
    collaborated_docs = db.session.query(document_collaborators.c.doc_id).filter(document_collaborators.c.user_id == user_id)

    # Consulta principal: excluir documentos donde el usuario es creador o colaborador
    docs = db.session.query(Document).filter(
        ~Document.doc_id.in_(created_docs),  # No ser creador
        ~Document.doc_id.in_(collaborated_docs)  # No ser colaborador
    ).all()

    return docs




    


