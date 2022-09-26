from utils.db import db


class Escuela(db.Model):
    id_escuela= db.Column(db.Integer, primary_key=True)
    codigo = db.Column(db.String(100))
    nombre = db.Column(db.String(100))
    duracion = db.Column(db.String(100))

    def __init__(self, codigo, nombre, duracion):
        self.codigo = codigo
        self.nombre = nombre
        self.duracion = duracion
