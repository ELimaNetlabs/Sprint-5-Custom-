from database.db_postgresql import db

class Snapshot(db.Model):
    __tablename__ = "snapshots"

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    document_id = db.Column(db.Integer, db.ForeignKey("documents.doc_id"), nullable=False)
    content = db.Column(db.Text, nullable=False)
    version = db.Column(db.Integer, nullable=False)

    def __init__(self, document_id, content):
        self.document_id = document_id
        self.content = content

    def to_dict(self):
        return {
            "id": self.id,
            "document_id": self.document_id,
            "content": self.content,
            "version": self.version
        }
