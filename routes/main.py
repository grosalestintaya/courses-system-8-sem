from flask import Blueprint, render_template, request, redirect, url_for, flash
from utils.db import db
from forms.form1 import NamerForm

mains = Blueprint("mains", __name__)


@mains.route("/")
def face():
    frist_name = "george rosales tintaya"
    stuff = "This is my examen"
    flash("this is my examen!")

    return render_template(
        "face.html",
        frist_name=frist_name,
        stuff=stuff,
    )


@mains.route("/mision_vision")
def mision_vision():
    return render_template(
        "about.html",
    )
