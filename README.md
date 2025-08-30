# Obesity Category Prediction Model

## Project Description
This project uses machine learning to predict obesity categories (**Normal weight**, **Obese**, **Overweight**, **Underweight**) based on input features such as **Age**, **Gender**, **Height**, **Weight**, **BMI**, and **Physical Activity Level**. Models like **Logistic Regression**, **Decision Tree**, and **XGBoost** are used, and the best model is deployed via a **Gradio** app for real-time predictions.

## Key Features:
- **Predict obesity category** based on user input.
- **Gradio Web App** for real-time predictions.
- **Multiple models**: Logistic Regression, Decision Tree, XGBoost.

---

## Live Demo:


## https://obesity-category-ksewzrxwtrgrcyrzgvdjdo.streamlit.app/


## App Photo:

<img width="1910" height="920" alt="image" src="https://github.com/user-attachments/assets/8513fff3-1bc8-45e6-89d5-8e47e14b03a6" />


## Installation

To install dependencies:

```bash
pip install -r requirements.txt


If you prefer installing individually, run:

pip install numpy pandas matplotlib seaborn scikit-learn xgboost gradio streamlit

Usage

Run the Gradio app to start the web interface:

python app.py


Access the app via:
Obesity Category Prediction App

Screenshot of the App


(Include a screenshot of your app here)

Model Training & Evaluation

Logistic Regression: Accuracy 96.5%

Decision Tree: Accuracy 100% (Overfitting possible)

XGBoost: Accuracy 98%, tuned with GridSearchCV

Best Parameters for XGBoost:

learning_rate = 0.1

max_depth = 3

n_estimators = 100

subsample = 0.8

Saving and Loading the Model
filename = 'trained_model.sav'
with open(filename, 'wb') as f:
    pickle.dump((best_model, scaler), f)

# Loading the saved model
loaded_model = pickle.load(open('trained_model.sav', 'rb'))

Contributing

Feel free to fork and improve the project:

Add new features or models.

Enhance the UI.
