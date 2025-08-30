# Obesity Category Prediction Model

## Project Description
This project uses machine learning to predict obesity categories (**Normal weight**, **Obese**, **Overweight**, **Underweight**) based on input features such as **Age**, **Gender**, **Height**, **Weight**, **BMI**, and **Physical Activity Level**. Models like **Logistic Regression**, **Decision Tree**, and **XGBoost** are used, and the best model is deployed via a **Gradio** app for real-time predictions.

## Key Features:
- **Predict obesity category** based on user input.
- **Gradio Web App** for real-time predictions.
- **Multiple models**: Logistic Regression, Decision Tree, XGBoost.

---

## Live Demo:


https://obesity-category-ksewzrxwtrgrcyrzgvdjdo.streamlit.app/


---

## App Screenshot:


<img width="1918" height="913" alt="image" src="https://github.com/user-attachments/assets/e90dd163-2dc5-4b87-a3ec-5353a85f3da5" />



---

## Installation

To install dependencies, you can either use the `requirements.txt` or install them individually.

1. **Using `requirements.txt`:**

```bash
pip install -r requirements.txt
Individually:

bash
Copy code
pip install numpy pandas matplotlib seaborn scikit-learn xgboost gradio streamlit
Usage
Run the Gradio app to start the web interface:

bash
Copy code
python app.py
Access the app in your browser at:

Obesity Category Prediction App

Model Training & Evaluation
Logistic Regression: Accuracy 96.5%

Decision Tree: Accuracy 100% (Note: potential overfitting)

XGBoost: Accuracy 98%, tuned using GridSearchCV

Best Parameters for XGBoost:
learning_rate = 0.1

max_depth = 3

n_estimators = 100

subsample = 0.8

Saving and Loading the Model
Once the model is trained, it is saved using pickle to avoid retraining each time. Here's how you can save and load the model:

Saving the Model:
python
Copy code
filename = 'trained_model.sav'
with open(filename, 'wb') as f:
    pickle.dump((best_model, scaler), f)
Loading the Model:
python
Copy code
loaded_model = pickle.load(open('trained_model.sav', 'rb'))
Contributing
Feel free to fork and improve the project! Here are a few ways you can contribute:

Add new features or models.

Enhance the UI of the Gradio app.

Improve documentation or write tests.

To contribute:

Fork the repository.

Create a new branch.

Make your changes and submit a pull request.
