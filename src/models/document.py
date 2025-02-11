from database.db_postgresql import db

document_collaborators = db.Table(
    "document_collaborators",
    db.Column("doc_id", db.String, db.ForeignKey("documents.doc_id"), primary_key=True),
    db.Column("user_id", db.String, db.ForeignKey("users.user_id"), primary_key=True),
)

class Document(db.Model):
    __tablename__ = "documents"

    doc_id = db.Column(db.String, primary_key=True)  
    name = db.Column(db.String, nullable=False)
    creator_id = db.Column(db.String, db.ForeignKey("users.user_id"), nullable=False)  
    content = db.Column(db.Text, default="")

    # Relación con el creador del documento
    creator = db.relationship("User", backref="created_documents")

    # Relación con colaboradores (Many-to-Many)
    collaborators = db.relationship("User", secondary=document_collaborators, backref="documents")

    def __init__(self, doc_id, name, creator_id, content=""):
        self.doc_id = doc_id
        self.name = name
        self.creator_id = creator_id
        self.content = content

    def to_dict(self):
        return {
            "doc_id": self.doc_id,
            "name": self.name,
            "creator_id": self.creator_id,
            "content": self.content,
            "collaborators": [user.user_id for user in self.collaborators]  # Lista de IDs de colaboradores
        }




