from utils.db import db
from models.escuela import Escuela

class Estudiante(db.Model):
    id_estudiante= db.Column(db.Integer, primary_key=True)
    id_escuela = db.Column(db.Integer, db.ForeignKey(Escuela.id_escuela))
    dni = db.Column(db.String(100))
    apellidos = db.Column(db.String(100))
    nombres = db.Column(db.String(100))
    fecNacimiento = db.Column(db.String(100))
    sexo= db.Column(db.String(10))

    def __init__(self, id_escuela,dni,apellidos,nombres,fecNacimiento,sexo):
        self.id_escuela = id_escuela
        self.dni = dni
        self.apellidos= apellidos
        self.nombres = nombres
        self.fecNacimiento = fecNacimiento
        self.sexo = sexo
