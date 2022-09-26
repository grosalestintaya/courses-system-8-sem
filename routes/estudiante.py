from flask import Blueprint, render_template, request, redirect, url_for, flash
from models.curso import Curso
from utils.db import db
from models.estudiante import Estudiante
from models.escuela import Escuela

estudiante = Blueprint("estudiante", __name__)


@estudiante.route("/showstudents")
def index():
    estudiantes = Estudiante.query.all()
    escuelas = Escuela.query.all()
    db.session.commit()
    return render_template(
        "student/index.html", estudiantes=estudiantes, escuelas=escuelas
    )


@estudiante.route("/newstudent", methods=["POST"])
def add_chool():
    if request.method == "POST":
        # recibiendo data del formulario
        nombre_escuela = request.form["nombre_escuela"]
        print(nombre_escuela)

        id_escuela = request.form["id_escuela"]
        dni = request.form["dni"]
        apellidos = request.form["apellidos"]
        nombres = request.form["nombres"]
        fecNacimiento = request.form["fecNacimiento"]
        sexo = request.form["sexo"]
        # creando un nuevo onjeto
        new_estudiante = Estudiante(
            id_escuela, dni, apellidos, nombres, fecNacimiento, sexo
        )
        # guardando el objeto en la base de datos
        db.session.add(new_estudiante)
        db.session.commit()

        flash("Student added successfully!")

        return redirect(url_for("estudiante.index"))


@estudiante.route("/updatestudent/<string:id>", methods=["GET", "POST"])
def update(id):
    # traer escuela by Id
    print(id)
    estudiante = Estudiante.query.get(id)
    escuelas = Escuela.query.all()

    if request.method == "POST":
        escuelas = Escuela.query.all()
        estudiante.id_escuela = request.form["id_escuela"]
        estudiante.dni = request.form["dni"]
        estudiante.apellidos = request.form["apellidos"]
        estudiante.nombres = request.form["nombres"]
        estudiante.feNacimiento = request.form["fecNacimiento"]
        estudiante.sexo = request.form["sexo"]
        db.session.commit()

        flash("student updated successfully!")

        return redirect(url_for("estudiante.index", escuelas=escuelas))

    return render_template(
        "student/update.html", estudiante=estudiante, escuelas=escuelas
    )


@estudiante.route("/deletestudent/<id>", methods=["GET"])
def delete(id):
    estudiante = Estudiante.query.get(id)
    db.session.delete(estudiante)
    db.session.commit()

    flash("School deleted successfully!")

    return redirect(url_for("curso.index"))


@estudiante.route(
    "/selectcoursetuitions/<id_estudiante>/<id_escuela>/<apellidos>/<nombres>", methods=["GET"]
)
def select(id_estudiante,id_escuela, apellidos, nombres):
    id_escuela = id_escuela
    id_estudiante = id_estudiante
    apellidos = apellidos
    nombres = nombres
    escuelas= Escuela.query.get(id_escuela)
    nombre_escuela=escuelas.nombre
    todos=Curso.query.all()

    return render_template(
        "tuition/index.html",
        id_escuela=id_escuela,
        apellidos=apellidos,
        nombres=nombres,
        nombre_escuela=nombre_escuela,
        todos=todos,
        id_estudiante=id_estudiante
    )
