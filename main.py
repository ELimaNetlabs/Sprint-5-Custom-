class Documento:
    def __init__(self, titulo, contenido):
        self.titulo = titulo
        self.contenido = contenido

class Usuario:
    def __init__(self, nombre, rol):
        self.nombre = nombre
        self.rol = rol

from flask import Flask, jsonify

app = Flask(__name__)

# Datos simulados
documentos = [
    {"id": 1, "titulo": "Documento 1", "contenido": "Este es el primer documento"},
    {"id": 2, "titulo": "Documento 2", "contenido": "Este es otro documento"}
]

@app.route("/documentos")
def obtener_documentos():
    return jsonify(documentos)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
