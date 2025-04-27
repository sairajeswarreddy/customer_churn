# Customer Churn Prediction - Flask Application

This project predicts whether a customer will churn (leave) based on their behavior and features.  
It uses Machine Learning and provides a simple Flask web application for predictions.

## 📄 Project Description

### Customer Churn Prediction

This project aims to predict customer churn (i.e., whether a customer is likely to leave or continue using a service) using machine learning techniques. The project utilizes a **Flask web application** to allow users to input customer data and receive a churn prediction.

#### **Machine Learning Model**
The model is trained on a dataset of customer information, including various features such as age, account tenure, and service usage patterns. We use **scikit-learn** to train a machine learning model that predicts if a customer is likely to churn based on these features.

#### **Flask Application**
The Flask application provides a simple **user interface** where users can input customer data and get a prediction on whether the customer is likely to churn. The app serves the trained machine learning model and uses it to provide real-time predictions.

## 🛠 Project Structure

- `customer_churn_prediction.ipynb` - Jupyter Notebook for training the ML model
- `app.py` - Flask app to run the prediction model
- `data.csv` - Dataset used for training
- `README.md` - Project documentation

## 🚀 How to Run the Project

1. **Clone the repository**
   ```bash
   git clone https://github.com/sairajeswarreddy/customer_churn.git
   cd customer_churn
