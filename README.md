
# Campus Placement Prediction

### Machine Learning-Based Student Placement Prediction System

A machine learning project developed to predict student campus placement outcomes using academic performance, educational background, work experience, and employability-related attributes. The project combines exploratory data analysis, classification models, and a Flask-based web application to provide predictions through an interactive interface.

## Project Overview

Campus placement is an important milestone for graduating students. This project explores how academic and background characteristics can be used to predict whether a student is likely to receive a placement offer.

The application accepts student information and returns one of two predictions:

- **Placed**
- **Not Placed**

**Project Type:** Undergraduate Academic Group Project (2 members)  
**Institution:** Sreenidhi Institute of Science and Technology  
**Discipline:** Data Science

## Technologies Used

- **Programming:** Python
- **Data Analysis:** Pandas, NumPy
- **Machine Learning:** Scikit-learn
- **Algorithms:** Random Forest Classifier, Logistic Regression
- **Web Development:** Flask, HTML, CSS
- **Development Environment:** Jupyter Notebook

## Dataset

The project uses a student placement dataset containing 215 records and 15 columns.

The dataset includes academic performance, educational background, work experience, employability test scores, specialization, and placement outcomes.

**Target Variable:** Placement Status (Placed / Not Placed)

The dataset is not included in this public repository because its original redistribution permissions have not been confirmed.

## Machine Learning Methodology

The project includes two classification approaches documented in separate notebooks.

### 1. Logistic Regression

The exploratory notebook demonstrates data preparation, feature processing, model training, and evaluation using Logistic Regression.

### 2. Random Forest Classifier

The model-training notebook uses a Random Forest Classifier to predict placement outcomes.

The trained model is saved as `place_model.pkl` and integrated into the Flask application.

The two notebooks use different preprocessing approaches and evaluation configurations, so their reported results should not be interpreted as a controlled comparison.

## Model Evaluation

The original notebook outputs report the following results:

| Model | Reported Accuracy | Reported F1-Score |
|---|---|---|
| Random Forest | Approximately 81% | 0.80 (weighted) |
| Logistic Regression | Approximately 85.94% | 0.8594 (micro) |

These are historical results from the original academic project and have not been independently reproduced for this portfolio.

## Flask Web Application

The Flask application provides an interface where users enter student details and request a placement prediction.

The application:

1. Collects student information through an HTML form.
2. Processes the submitted input values.
3. Uses the saved machine learning model to generate a prediction.
4. Displays the predicted placement outcome.

### Application Screenshots

Screenshots of the original application, including input forms and both prediction outcomes, are available in the [`ScreenShots`](ScreenShots/) folder.

## Repository Contents

- `app.py` — Flask application
- `place_model.ipynb` — Random Forest model development
- `grpprjct.ipynb` — Exploratory analysis and Logistic Regression
- `place_model.pkl` — Saved model artifact
- `templates/` — HTML interface and supporting assets
- `ScreenShots/` — Application screenshots
- `.gitignore` — Python Git exclusions

## Running the Application

This repository preserves the original academic implementation.

The application uses Python, Flask, Joblib, and Scikit-learn. The saved model is loaded from `place_model.pkl`.

After installing the required dependencies in a compatible Python environment, run:

```bash
python app.py
```

The Flask development server is configured to run locally. Open the local address displayed in the terminal.

**Note:** The original environment and dependency versions have not been fully reconstructed. The training dataset is not distributed, and the application has not been independently retested in a clean environment. Load saved model files only when you trust their source.

## Team Collaboration

This project was developed as a **two-member undergraduate academic project**.

The work involved dataset exploration, machine learning model development, application implementation, testing, and academic documentation.

## Project Documentation

The original academic project report is maintained privately to protect student and institutional information.

## Project Scope

This is an academic prototype intended to demonstrate the application of machine learning to placement prediction. It is not intended to be used as an automated real-world hiring or student selection system.
