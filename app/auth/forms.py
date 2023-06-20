from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField
from wtforms.validators import DataRequired, EqualTo

class PokeName(FlaskForm):
    pokemon = StringField('Enter Pokemon', validators=[DataRequired()])
    submit = SubmitField()