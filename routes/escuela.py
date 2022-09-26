from flask import Blueprint, render_template, request, redirect, url_for, flash
from utils.db import db
from models.escuela import Escuela

escuela = Blueprint("escuela", __name__)


@escuela.route("/showschools")
def index():
    escuelas = Escuela.query.all()
    db.session.commit()

    return render_template("school/index.html",escuelas=escuelas)
@escuela.route("/newschool", methods=["POST"])
def add_chool():
    if request.method == "POST":
        # recibiendo sata del formulario
        codigo = request.form["codigo"]
        nombre = request.form["nombre"]
        duracion = request.form["duracion"]
        # creando un nuevo onjeto
        new_escuela = Escuela(codigo, nombre, duracion)
        # guardando el objeto en la base de datos
        db.session.add(new_escuela)
        db.session.commit()

        flash("School added successfully!")

        return redirect(url_for("escuela.index"))


@escuela.route("/updateschool/<string:id>", methods=["GET", "POST"])
def update(id):
    # traer escuela by Id
    print(id)
    escuela = Escuela.query.get(id)

    if request.method == "POST":
        escuela.codigo = request.form["codigo"]
        escuela.nombre = request.form["nombre"]
        escuela.duracion = request.form["duracion"]

        db.session.commit()

        flash("School updated successfully!")

        return redirect(url_for("escuela.index"))

    return render_template("school/update.html", escuela=escuela)


@escuela.route("/deleteschool/<id>", methods=["GET"])
def delete(id):
    escuela = Escuela.query.get(id)
    db.session.delete(escuela)
    db.session.commit()

    flash("School deleted successfully!")

    return redirect(url_for("escuela.index"))
