# Heart Disease Prediction Project 🚑❤️

## Project Overview
The **Heart Disease Prediction** project aims to develop a machine learning model that can predict whether an individual is at risk of heart disease based on various health parameters. Cardiovascular diseases are one of the leading causes of death worldwide, and early detection can play a significant role in saving lives. This project leverages supervised machine learning techniques to help healthcare professionals and individuals understand the risk of heart disease, enabling timely interventions.

## Dataset
The dataset contains health records of individuals, including several clinical parameters. Below are the attributes used for prediction:

1. **Age**: Age of the patient.
2. **Sex**: Gender of the patient (1 for Male, 0 for Female).
3. **Chest Pain Type (CP)**:
   - Value 1: Typical angina (chest pain related to decreased blood supply to the heart).
   - Value 2: Atypical angina (pain not related to the heart).
   - Value 3: Non-anginal pain (pain not related to heart issues).
   - Value 4: Asymptomatic.
4. **Resting Blood Pressure (trtbps)**: Resting blood pressure in mm Hg.
5. **Cholesterol (chol)**: Serum cholesterol in mg/dl.
6. **Fasting Blood Sugar (FBS)**: Whether the fasting blood sugar is greater than 120 mg/dl (1 = True; 0 = False).
7. **Resting Electrocardiographic Results (restecg)**:
   - Value 0: Normal.
   - Value 1: Having ST-T wave abnormality (T wave inversions and/or ST elevation or depression of > 0.05 mV).
   - Value 2: Showing probable or definite left ventricular hypertrophy by Estes' criteria.
8. **Max Heart Rate Achieved (thalachh)**: Maximum heart rate achieved during exercise.
9. **Exercise Induced Angina (exng)**: Whether exercise-induced angina occurred (1 = Yes; 0 = No).
10. **Old Peak (oldpeak)**: ST depression induced by exercise relative to rest.
11. **Slope (slp)**: The slope of the peak exercise ST segment.
12. **Number of Major Vessels (caa)**: Number of major vessels (0-3) colored by fluoroscopy.
13. **Thallium Stress Test Result (thall)**:
    - Value 0: Normal.
    - Value 1: Fixed defect.
    - Value 2: Reversible defect.

The **output variable** indicates the presence of heart disease:
- **1**: The patient is at risk of heart disease.
- **0**: The patient is not at risk of heart disease.

## Objective
The main goal of this project is to build a predictive model that can assess the risk of heart disease based on a patient's clinical features. This is achieved by training a classification model on labeled data.

## Approach
### 1. Data Preprocessing
- **Data Cleaning**: Handling missing values, outliers, and ensuring data consistency.
- **Feature Scaling**: StandardScaler was used to bring features like age, blood pressure, and cholesterol to a similar scale.
- **Feature Selection**: Techniques like Lasso and ElasticNet were used to identify the most significant features affecting heart disease.

### 2. Model Selection and Training
- Various machine learning algorithms were tested, including **Decision Trees**, **Logistic Regression**, **Random Forest**, and **Gradient Boosting**.
- **GridSearchCV** was used to fine-tune hyperparameters and select the best performing model.
- Cross-validation was applied to evaluate model performance and avoid overfitting.

### 3. Model Evaluation
- Metrics such as **Accuracy**, **Precision**, **Recall**, and **F1 Score** were used to evaluate the model's performance.
- The best model achieved an accuracy of **72%** with cross-validation results indicating a consistent performance range between **65% and 72%**.

### 4. Deployment
- The model was deployed using a **Flask** web application hosted on **Render**.
- The web app has a user-friendly interface where users can input health parameters to predict the risk of heart disease.

## How to Run the Project
### Requirements
- **Python 3.8+**
- **Flask** for the web application
- **scikit-learn**, **pandas**, and **numpy** for model building and data manipulation

### User Interface
The web application provides a form where users can input different health parameters such as age, cholesterol levels, blood pressure, etc. Upon submission, the model predicts whether the patient is at risk of heart disease and displays the result.

### Insights
Chest Pain Type (CP) and Number of Major Vessels (caa) were found to be highly significant in determining heart disease risk.
Individuals with exercise-induced angina (exng) and a high oldpeak value were more likely to be at risk.
The model demonstrated that max heart rate achieved (thalachh) plays a critical role in predicting the risk of heart disease.
### Future Work
Improve Model Accuracy: Test additional models like XGBoost or Deep Learning models for improved performance.
### Collect More Data: Increasing the dataset size could help improve the accuracy and reliability of the model.
Feature Engineering: Extract more meaningful features from the existing data to enhance model predictions.
User Authentication: Add login and security features to make the web application more robust for real-world use.
Conclusion
This project serves as an example of how machine learning can be applied to healthcare to provide timely predictions and save lives. The current model provides a good starting point for understanding the factors affecting heart disease and gives an early risk assessment tool for individuals and healthcare professionals.


