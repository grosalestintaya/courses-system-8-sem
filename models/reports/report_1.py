from utils.db import db

class reportTuition(db.Model):
    id_report = db.Column(db.Integer, primary_key=True)
    apellidos = db.Column(db.String(100))
    nombres = db.Column(db.String(100))
    nombre_escuela = db.Column(db.String(100))
    nombre_curso = db.Column(db.String(100))
    creditos = db.Column(db.String(100))


    def __init__(self, apellidos, nombres, nombre_escuela,nombre_curso,creditos):
      self.apellidos = apellidos
      self.nombres = nombres
      self.nombre_escuela = nombre_escuela
      self.nombre_curso = nombre_curso
      self.creditos = creditos