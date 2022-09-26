from utils.db import db
from models.escuela import Escuela



class Curso(db.Model):
    
    id_curso = db.Column(db.Integer, primary_key=True)
    id_escuela = db.Column(db.Integer, db.ForeignKey(Escuela.id_escuela))
    codigo = db.Column(db.String(100))
    nombre = db.Column(db.String(100))
    credito = db.Column(db.String(100))

    def __init__(self,id_escuela,codigo,nombre,credito):
        self.id_escuela = id_escuela
        self.codigo = codigo
        self.nombre = nombre
        self.credito = credito
