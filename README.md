## Live Demo:

## https://obesity-category-ksewzrxwtrgrcyrzgvdjdo.streamlit.app/

## App Photo:


<img width="1918" height="913" alt="Screenshot 2025-08-30 143732" src="https://github.com/user-attachments/assets/9e9239cd-b8c1-46fb-85eb-575b35fa9c64" />



# Obesity Category

This project aims to classify obesity categories based on given health metrics and data. The goal is to help identify the obesity status of individuals using various features, such as body mass index (BMI), age, gender, and other relevant factors.

## Table of Contents

- [Introduction](#introduction)
- [Installation](#installation)
- [Usage](#usage)
- [Data](#data)
- [Models](#models)
- [Contributing](#contributing)
- [License](#license)

## Introduction

This project provides a machine learning-based solution to classify individuals into different obesity categories (e.g., underweight, normal weight, overweight, obese) using their health and demographic data.

## Installation

To run this project locally, follow these steps:

1. Clone the repository:

    ```bash
    git clone https://github.com/KishoreR2k7/Obesity-Category.git
    cd Obesity-Category
    ```

2. Install the required dependencies:

    ```bash
    pip install -r requirements.txt
    ```

3. Make sure you have Python 3.x and the necessary libraries installed:

    - pandas
    - numpy
    - scikit-learn
    - matplotlib
    - seaborn

    You can install them manually if they aren't listed in `requirements.txt`:

    ```bash
    pip install pandas numpy scikit-learn matplotlib seaborn
    ```

## Usage

### Train a Model

1. To train a model, simply run the `train.py` script:

    ```bash
    python train.py
    ```

2. This will process the dataset, train the model, and save the output.

### Predict Obesity Category

Once the model is trained, you can use it to predict obesity categories based on new data.

1. Use the `predict.py` script:

    ```bash
    python predict.py --input data/input_data.csv
    ```

2. Replace `input_data.csv` with the data you wish to classify.

## Data

The dataset used in this project contains information about individuals' health, including the following features:

- Age
- Gender
- BMI
- Waist circumference
- Height
- Weight

You can find the dataset in the `data/` directory or use a custom dataset that follows the same structure.

## Models

This project uses machine learning algorithms to classify obesity categories. Some models implemented include:

- Logistic Regression
- Decision Trees
- Random Forest
- Support Vector Machines (SVM)

You can modify or add more models by editing the `train.py` script.

## Contributing

If you'd like to contribute to this project, feel free to fork the repository and submit a pull request. Please ensure that your contributions align with the following guidelines:

1. Fork the repo and create a new branch.
2. Make your changes and commit them with meaningful messages.
3. Push your changes to your forked repo and create a pull request.
