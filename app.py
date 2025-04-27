import pickle
import numpy as np
from flask import Flask, render_template, request

# Load model
with open('rf_model.pkl', 'rb') as file:
    model = pickle.load(file)

# Load column names (features)
with open('model_columns.pkl', 'rb') as file:
    model_columns = pickle.load(file)

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def predict():
    prediction = None
    if request.method == 'POST':
        # Collect form inputs, ensuring the order matches the trained model's feature set
        data = [
            float(request.form['CreditScore']),       # CreditScore
            float(request.form['Age']),               # Age
            float(request.form['Tenure']),            # Tenure
            float(request.form['Balance']),           # Balance
            float(request.form['NumOfProducts']),     # NumOfProducts
            float(request.form['HasCrCard']),         # HasCrCard
            float(request.form['IsActiveMember']),    # IsActiveMember
            float(request.form['EstimatedSalary']),   # EstimatedSalary
            1 if request.form['Geography'] == 'Germany' else 0,  # Geography_Germany
            1 if request.form['Geography'] == 'Spain' else 0,    # Geography_Spain
            1 if request.form['Gender'] == 'Male' else 0   # Gender_Male
        ]

        # Reshape and predict
        final_input = np.array(data).reshape(1, -1)
        result = model.predict(final_input)
        prediction = "Yes" if result[0] == 1 else "No"
    
    return render_template('index.html', prediction=prediction)

if __name__ == '__main__':
    app.run(debug=True)
