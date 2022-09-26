
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.validators import DataRequired

class NamerForm(FlaskForm):
    name = StringField("What's your Name", validators=[DataRequired()])
    submit = SubmitField('Submit')