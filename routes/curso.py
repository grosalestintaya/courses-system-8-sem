from flask import Blueprint, render_template, request, redirect, url_for, flash
from utils.db import db
from models.curso import Curso 
from models.escuela import Escuela

curso = Blueprint("curso", __name__)

@curso.route("/showscourses")
def index():
    cursos = Curso.query.all()
    escuelas= Escuela.query.all()
    db.session.commit()
    return render_template("course/index.html",cursos=cursos,escuelas=escuelas)
@curso.route("/newscourse", methods=["POST"])
def add_chool():
    if request.method == "POST":
        # recibiendo data del formulario
        id_escuela = request.form["id_escuela"]
        codigo = request.form["codigo"]
        nombre = request.form["nombre"]
        credito = request.form["credito"]
        # creando un nuevo onjeto
        new_curso = Curso(id_escuela,codigo, nombre, credito)
        # guardando el objeto en la base de datos
        db.session.add(new_curso)
        db.session.commit()

        flash("School added successfully!")

        return redirect(url_for("curso.index"))


@curso.route("/updatecourse/<string:id>", methods=["GET", "POST"])
def update(id):
    # traer escuela by Id
    print(id)
    curso = Curso.query.get(id)

    if request.method == "POST":
        curso.id_escuela = request.form["id_curso"]
        curso.id_escuela = request.form["id_escuela"]
        curso.codigo = request.form["codigo"]
        curso.nombre = request.form["nombre"]
        curso.credito = request.form["credito"]

        db.session.commit()

        flash("School updated successfully!")

        return redirect(url_for("curso.index"))

    return render_template("course/update.html", curso=curso)


@curso.route("/deletecourse/<id>", methods=["GET"])
def delete(id):
    curso = Curso.query.get(id)
    db.session.delete(curso)
    db.session.commit()

    flash("School deleted successfully!")

    return redirect(url_for("curso.index"))
 