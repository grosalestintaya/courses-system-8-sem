from utils.db import db
from models.curso import Curso
from models.escuela import Escuela
from models.estudiante import Estudiante 
from sqlalchemy.ext.declarative import declarative_base
Base = declarative_base()


class Matricula(db.Model):
    id_matricula= db.Column(db.Integer, primary_key=True)
    id_curso = db.Column(db.Integer, db.ForeignKey(Curso.id_curso))
    id_escuela = db.Column(db.Integer, db.ForeignKey(Escuela.id_escuela))
    id_estudiante = db.Column(db.Integer, db.ForeignKey(Estudiante.id_estudiante))

    def __init__(self, id_curso, id_escuela, id_estudiante):
        self.id_curso = id_curso
        self.id_escuela = id_escuela
        self.id_estudiante = id_estudiante
 