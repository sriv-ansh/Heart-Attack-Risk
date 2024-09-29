from flask import Flask, request, render_template
import pickle
import joblib
import pandas as pd

app = Flask(__name__)

# Load the Feature Scaling File
with open("Feature Scaler File/StandardScaler.pkl", "rb") as ss_file:
    ss = pickle.load(ss_file)

# Load the Model File
with open("ML Model/DecisionTree_Model.yml", "rb") as model_file:
    model = pickle.load(model_file)

# Route for Index Page
@app.route('/')
def index():
    return render_template('Main_Page.html')

# Route for Prediction
@app.route('/predict', methods=['POST'])
def predict():
    # Retrieve the Data
    age = int(request.form.get('age'))
    sex = int(request.form.get('sex'))
    cp = int(request.form.get('cp'))
    trtbps = int(request.form.get('trtbps'))
    chol = int(request.form.get('chol'))
    fbs = int(request.form.get('fbs'))
    restecg = int(request.form.get('restecg'))
    thalachh = int(request.form.get('thalachh'))
    exng = int(request.form.get('exng'))
    oldpeak = float(request.form.get('oldpeak'))
    slp = int(request.form.get('slp'))
    caa = int(request.form.get('caa'))
    thall = int(request.form.get('thall'))

    # Create the input data
    input_data = pd.DataFrame({
        'age': [age], 'sex': [sex],
        'cp': [cp], 'trtbps': [trtbps],
        'chol': [chol], 'fbs': [fbs],
        'restecg': [restecg], 'thalachh': [thalachh],
        'exng': [exng], 'oldpeak': [oldpeak],
        'slp': [slp], 'caa': [caa], 'thall': [thall]
    })

    # Apply feature scaling
    input_data[['age', 'trtbps', 'chol', 'thalachh']] = ss.transform(input_data[['age', 'trtbps', 'chol', 'thalachh']])

    # Prediction
    prediction = model.predict(input_data)

    if prediction[0] == 1:
        result = "The patient has a high risk of heart disease."
    else:
        result = "The patient has a low risk of heart disease."

    return render_template('Result_Page.html', result=result)

if __name__ == '__main__':
    app.run(debug=True)
