from flask_wtf import FlaskForm
from wtforms import StringField,   SubmitField
from wtforms.validators import DataRequired

class ModelePredictionForm(FlaskForm):
    taille = StringField('Taille', validators=[DataRequired()])
    poids = StringField('Poids', validators=[DataRequired()])
    pointure = StringField('Pointure', validators=[DataRequired()])

    submit = SubmitField('Prédire')