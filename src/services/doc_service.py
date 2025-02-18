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
    created_docs = db.session.query(Document.doc_id).filter(Document.creator_id == user_id)

    collaborated_docs = db.session.query(document_collaborators.c.doc_id).filter(document_collaborators.c.user_id == user_id)

    docs = db.session.query(Document).filter(
        ~Document.doc_id.in_(created_docs),  
        ~Document.doc_id.in_(collaborated_docs)  
    ).all()

    return docs

def create_doc(title, creator):
    
    new_doc = Document(title=title, creator_id=creator)
    db.session.add(new_doc)
    db.session.commit()
    return new_doc

def update_doc(doc_id):
    # Obtener el documento a actualizar
    document = Document.query.get_or_404(doc_id)

    # Obtener los datos del formulario
    new_title = request.form.get("title")
    new_content = request.form.get("content")

    # Actualizar el documento con los nuevos datos
    document.title = new_title
    document.content = new_content

    # Guardar los cambios en la base de datos
    try:
        db.session.commit()
        flash("Documento actualizado correctamente.", "success")
    except Exception as e:
        db.session.rollback()
        flash("Error al actualizar el documento.", "danger")
        print(f"Error: {e}")

    # Redirigir al editor o a otra ruta, por ejemplo, al menú de documentos
    return redirect(url_for("document.editor", doc_id=doc_id))