from app import app
from flask import render_template
import pickle, numpy as np
from joblib import dump, load
#from sklearn.linear_model import LinearRegression

@app.route('/')
@app.route('/index')
def index():
    modeles = {'titre': 'KNN'}
    parametres = [
        {"par1":"10", "par2":"uniform"},
        {"par1":"20", "par2":"lineaire"}
    ]
    return render_template('index.html', titre_page='Accueil', mod=modeles, page_no=1, param=parametres)

from app.forms import ModelePredictionForm

from flask import  flash, redirect

@app.route('/form_input', methods=['GET', 'POST'])
def form_input():
    form = ModelePredictionForm()
    if form.validate_on_submit():
        #formuler le data
        sample_data = [form.taille.data, form.poids.data, form.pointure.data]
        clean_data = [float(i) for i in sample_data]
        data = []
        data.extend(clean_data[0:3])
        # Reshape the Data
        ex1 = np.array(data).reshape(1, -1)
        #lire le modele
        #rl_model = pickle.load(open('modele_LR.pkl', 'rb'))
        rl_model = load("knn.joblib")
        resultat_prediction = rl_model.predict(ex1)
        flash('Taille: {}, Poids:{}, Pointure:{} donne Y={}'.format(
            form.taille.data, form.poids.data, form.pointure.data, resultat_prediction))
        return redirect('/index')
    return render_template('form_input.html', title='Modele de Prediction', form=form)




