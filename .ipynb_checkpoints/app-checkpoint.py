from flask import Flask, render_template, request
import joblib
import numpy as np
import pandas as pd

app = Flask(__name__)

# Load trained components
model = joblib.load("weather_model.pkl")
scaler = joblib.load("scaler.pkl")
le = joblib.load("label_encoder.pkl")

# Feature columns (must match training order)
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

# Home route
@app.route('/')
def home():
    return render_template("index.html")


# Prediction route
@app.route('/predict', methods=['POST'])
def predict():
    try:
        values = []

        # Get input values safely
        for col in columns:
            val = request.form.get(col)

            if val is None or val.strip() == "":
                return render_template(
                    "index.html",
                    prediction_text="⚠️ Please enter all values"
                )

            values.append(float(val))

        # Convert to DataFrame
        df = pd.DataFrame([values], columns=columns)

        # Apply scaling (same as training)
        df_scaled = scaler.transform(df.values)

        # Predict
        prediction = model.predict(df_scaled)

        # Decode label
        output = le.inverse_transform(prediction)

        result = "Predicted Weather: " + output[0]

    except Exception as e:
        result = f"Error: {str(e)}"

    return render_template("index.html", prediction_text=result)


# Run app
if __name__ == "__main__":
    app.run(debug=True)