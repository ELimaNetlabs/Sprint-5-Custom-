from database.db_postgresql import db
from models.document import Document
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
    


