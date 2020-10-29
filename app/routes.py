from app import app
from flask import render_template
import pickle, numpy as np
import pandas as pd
from joblib import dump, load
#from sklearn.linear_model import LinearRegression

# @app.route('/')
# @app.route('/index')
# def index():
    # modeles = {'titre': 'France'}
    # parametres = [
        # {"par1":"10", "par2":"uniform"},
        # {"par1":"20", "par2":"lineaire"}
    # ]
    # return render_template('index.html', titre_page='Accueil', mod=modeles, page_no=1, param=parametres)

from app.forms import ModelePredictionForm

from flask import  flash, redirect

@app.route('/', methods=['GET', 'POST'])
def form_input():
    form = ModelePredictionForm()
    if form.validate_on_submit():

        colnames = ["latitude","longitude","nombre_pieces_principales","surface_reelle_bati","surface_terrain","type_local"]
        sample_data = [form.latitude.data, form.longitude.data,
                        form.nombre_pieces_principales.data, form.surface_reelle_bati.data,
                        form.surface_terrain.data,form.type_local.data]
        X_df = pd.DataFrame([sample_data],columns=colnames)
        
        
        pred_model = load("model.joblib")
        resultat_prediction = pred_model.predict(X_df)
        resultat_prediction = np.expm1(resultat_prediction[0])
        prediction_text="Valeur estimée : {:.0f} $".format(resultat_prediction)

        flash(prediction_text)

        #return redirect('/')
    return render_template('form_input.html', title='Modele de Prediction', form=form)




