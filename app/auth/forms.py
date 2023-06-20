from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.validators import DataRequired

class PokeName(FlaskForm):
    pokemon = StringField('Enter Pokemon', validators=[DataRequired()])
    submit = SubmitField()