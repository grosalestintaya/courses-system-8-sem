from flask import Flask
from routes.main import mains
from routes.curso import curso
from routes.escuela import escuela
from routes.estudiante import estudiante
from routes.matricula import matricula
from flask_sqlalchemy import SQLAlchemy
from config import DATABASE_CONNECTION_URI

app = Flask(__name__)

# settings
app.secret_key = "mysecret"
print(DATABASE_CONNECTION_URI)
app.config["SQLALCHEMY_DATABASE_URI"] = DATABASE_CONNECTION_URI
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False

# no cache
app.config["SEND_FILE_MAX_AGE_DEFAULT"] = 0

SQLAlchemy(app)
app.register_blueprint(escuela)
app.register_blueprint(mains)
app.register_blueprint(curso)
app.register_blueprint(estudiante)
app.register_blueprint(matricula)
