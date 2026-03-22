from flask import Flask, render_template, request
import joblib
import numpy as np
import pandas as pd

app = Flask(__name__)

model = joblib.load("weather_model.pkl")

scaler = joblib.load("scaler.pkl")

le = joblib.load("label_encoder.pkl")


columns = [

'umbrella_sales',
'raincoat_sales',
'icecream_sales',
'cold_drink_sales',
'sunscreen_sales',
'jacket_sales',
'heater_sales',
'sweater_sales',
'gloves_sales',
'tea_sales',
'coffee_sales',
'soup_sales',
'snacks_sales',
'bread_sales'

]


@app.route('/')

def home():

    return render_template("index.html")


@app.route('/predict',methods=['POST'])

def predict():

    values = []

    for col in columns:

        values.append(float(request.form[col]))

    df = pd.DataFrame([values],columns=columns)

    df = scaler.transform(df)

    prediction = model.predict(df)

    output = le.inverse_transform(prediction)

    return render_template(
        "index.html",
        prediction_text="Predicted Weather: "+output[0]
    )


if __name__ == "__main__":

    app.run(debug=True)
