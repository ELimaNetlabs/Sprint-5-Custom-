from database.db_postgresql import db

document_collaborators = db.Table(
    "document_collaborators",
    db.Column("doc_id", db.Integer, db.ForeignKey("documents.doc_id"), primary_key=True),
    db.Column("user_id", db.Integer, db.ForeignKey("users.user_id"), primary_key=True),
)

class Document(db.Model):
    __tablename__ = "documents"

    doc_id = db.Column(db.Integer, primary_key=True, autoincrement=True) 
    title = db.Column(db.String, nullable=False)
    creator_id = db.Column(db.Integer, db.ForeignKey("users.user_id"), nullable=False)  
    content = db.Column(db.Text, default="")

    # Relación con el creador del documento
    creator = db.relationship("User", backref="created_documents")

    # Relación con colaboradores (Many-to-Many)
    collaborators = db.relationship("User", secondary=document_collaborators, backref="documents")

    def __init__(self, title, creator_id, content=""):
        self.title = title
        self.creator_id = creator_id
        self.content = content

    def to_dict(self):
        return {
            "doc_id": self.doc_id,
            "title": self.title,
            "creator_id": self.creator_id,
            "content": self.content,
            "collaborators": [user.user_id for user in self.collaborators]  # Lista de IDs de colaboradores
        }




