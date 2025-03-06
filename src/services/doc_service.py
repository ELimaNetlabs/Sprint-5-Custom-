from database.db_postgresql import db
from datetime import datetime
from models.document import Document, document_collaborators
from models.user import User  
from models.snapshot import Snapshot

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
    created_docs = db.session.query(Document.doc_id).filter(Document.creator_id == user_id)

    collaborated_docs = db.session.query(document_collaborators.c.doc_id).filter(document_collaborators.c.user_id == user_id)

    docs = db.session.query(Document).filter(~Document.doc_id.in_(created_docs),  ~Document.doc_id.in_(collaborated_docs)).all()

    return docs

def create_doc(title, creator):
    
    new_doc = Document(title=title, creator_id=creator)
    db.session.add(new_doc)
    db.session.commit()
    return new_doc

def update_doc(doc_id, title, content):
    document = get_doc_by_id(doc_id)

    last_snapshot = Snapshot.query.filter_by(document_id=doc_id).order_by(Snapshot.version.desc()).first()

    if not last_snapshot and len(content) >= 100:
        first_snapshot = Snapshot(document_id=doc_id, content=content)
        first_snapshot.version = 1  
        db.session.add(first_snapshot)


    elif last_snapshot and len(content) - len(last_snapshot.content) >= 100:
        new_snapshot = Snapshot(document_id=doc_id, content=content)
        new_snapshot.version = last_snapshot.version + 1
        db.session.add(new_snapshot)

    document.title = title
    document.content = content

    try:
        db.session.commit()
        return True
    except Exception as e:
        db.session.rollback()
        return False


    
def collaborate(doc_id, user_id):
    document = Document.query.get(doc_id)
    user = User.query.get(user_id)

    if document and user:
        document.collaborators.append(user)
        
        db.session.commit()
        return True
    
    return False
