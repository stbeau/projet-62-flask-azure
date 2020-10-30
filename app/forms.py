from flask_wtf import FlaskForm
from wtforms import StringField, FloatField, SubmitField
from wtforms.validators import DataRequired

class ModelePredictionForm(FlaskForm):
    type_local = StringField('Type de local', validators=[DataRequired()])
    nombre_pieces_principales = FloatField('Nombre de pieces principales', validators=[DataRequired()])
    surface_reelle_bati = FloatField('Surface réelle bati', validators=[DataRequired()])
    surface_terrain = FloatField('Surface du terrain', validators=[DataRequired()])
    latitude = FloatField('LAtitude', validators=[DataRequired()])
    longitude = FloatField('Longitude', validators=[DataRequired()])

    submit = SubmitField('Prédire')