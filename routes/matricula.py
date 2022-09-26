from flask import Blueprint, render_template, request, redirect, url_for, flash
from models.curso import Curso
from utils.db import db
from models.matricula import Matricula
from models.reports.report_1 import reportTuition

matricula = Blueprint("matricula", __name__)

@matricula.route("/showsreport")
def show():
    reports= reportTuition.query.all()
    db.session.commit()
    return render_template("tuition/show_index.html",reports=reports)

@matricula.route("/newtuition", methods=["POST"])
def newtuition():
    if request.method == "POST":
        # recive datos del formulario para  matricula
        id_curso = request.form["id_curso"]
        id_escuela = request.form["id_escuela"]
        id_estudiante = request.form["id_estudiante"]
        nombrecur=Curso.query.get(id_curso)
        nombre_curso=nombrecur.nombre
        creditos=nombrecur.credito
        print(nombre_curso)

                # creando un nuevo objeto matricula
        new_matricula = Matricula(id_curso, id_escuela, id_estudiante)
        # recive datos del formulario para  reporte
        apellidos = request.form["apellidos"]
        nombres = request.form["nombres"]
        nombre_escuela = request.form["nombre_escuela"]
    
        # creando un nuevo objeto reporte matricula
        new_report = reportTuition(apellidos, nombres, nombre_escuela,nombre_curso,creditos)
        # guardando objetos en la base de datos
        db.session.add(new_matricula)
        db.session.add(new_report)
        db.session.commit()

        flash("Tuition added successfully!")

        return redirect(url_for("estudiante.index"))


