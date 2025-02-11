class Document:
    def __init__(self, doc_id: str, name: str, creator: str, content: str = ""): 
        self.doc_id = doc_id  
        self.name = name  
        self.creator = creator
        self.content = content  
        self.historial_ediciones: List[Dict] = []  