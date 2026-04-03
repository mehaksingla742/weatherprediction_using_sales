# Weather Prediction using Product Sales Data 🌦️📊

## Project Description

This project predicts weather conditions (**Cloudy, Cold, Rainy, Sunny**) using the sales data of different products. The idea behind this project is that customer buying behavior depends on weather conditions. By analyzing these sales patterns, we can train a machine learning model to predict the weather.

For example:

* High umbrella and raincoat sales → Rainy weather
* High ice cream and cold drink sales → Sunny weather
* High jacket and heater sales → Cold weather
* Moderate mixed sales → Cloudy weather

## Dataset Features

The dataset contains the following input features:

| Feature Name     | Description              |
| ---------------- | ------------------------ |
| umbrella_sales   | Number of umbrellas sold |
| raincoat_sales   | Number of raincoats sold |
| icecream_sales   | Ice cream sales          |
| cold_drink_sales | Cold drink sales         |
| sunscreen_sales  | Sunscreen sales          |
| jacket_sales     | Jacket sales             |
| heater_sales     | Heater sales             |
| sweater_sales    | Sweater sales            |
| gloves_sales     | Gloves sales             |
| tea_sales        | Tea sales                |
| coffee_sales     | Coffee sales             |
| soup_sales       | Soup sales               |
| bread_sales      | Bread sales              |
| snacks_sales     | Snacks sales             |

### Target Variable

Weather condition:

* Cloudy
* Cold
* Rainy
* Sunny

## Project Workflow

### 1 Data Collection

Collected product sales data and weather labels.

### 2 Data Preprocessing

* Removed missing values
* Handled null values
* Removed duplicates
* Verified data types

### 3 Exploratory Data Analysis

Studied relationship between weather and product demand.

Examples:

* Rainy → umbrella ↑ raincoat ↑ snacks ↑
* Sunny → icecream ↑ cold drinks ↑ sunscreen ↑
* Cold → jacket ↑ heater ↑ tea ↑ coffee ↑ soup ↑ bread ↑
* Cloudy → balanced sales

### 4 Model Building

Machine Learning models used:

* Decision Tree Classifier
* Random Forest Classifier
* KNN Algorithm

### 5 Model Evaluation

Performance evaluated using:

* Accuracy Score
* Confusion Matrix
* Classification Report

### 6 Prediction

The model predicts weather based on new product sales input.

#Screenshots of Project
<img width="1920" height="849" alt="image" src="https://github.com/user-attachments/assets/322d78e9-ff6c-4e59-a88b-79facc925b54" />
<img width="1914" height="868" alt="image" src="https://github.com/user-attachments/assets/fa20c5d5-8f18-4a09-91f0-c7705faba22f" />


## Technologies Used

* Python
* Pandas
* NumPy
* Matplotlib
* Scikit-learn
* Jupyter Notebook

## How to Run the Project

### Clone repository

git clone https://github.com/mehaksingla742/weatherprediction_using_sales.git

### Install libraries

pip install pandas numpy matplotlib scikit-learn

### Run project

Open Jupyter Notebook and run the notebook file.

## Example Prediction

Input:
umbrella_sales = 85
raincoat_sales = 70
icecream_sales = 12
heater_sales = 8
bread_sales = 40

Output:
Rainy Weather

## Applications

* Retail demand forecasting
* Inventory management
* Business intelligence
* Weather estimation through consumer behavior
* Sales analytics

## Future Improvements

* Increase dataset size
* Try Gradient Boosting
* Deploy using Streamlit
* Add Power BI dashboard

## Author

Mehak

## Conclusion

This project shows how product sales patterns can help in predicting weather conditions using machine learning.

## License

Educational Project
