# Build Model with Feature Validation Pipeline

## Project Overview

-This project is a Machine Learning based Depression Prediction System integrated with a Feature Validation Pipeline and Data Drift Detection.

-The system validates incoming user data before sending it to the trained model for prediction. This helps improve model reliability and prevents incorrect predictions caused by invalid or poor-quality data.

-The project also uses Evidently AI for monitoring and detecting data drift between training data and new incoming data.

---

# Features

* Depression prediction using Machine Learning
* Feature validation pipeline
* Missing value checking
* Invalid value detection
* FastAPI integration
* Data drift detection using Evidently AI
* REST API for real-time prediction
* Production-style project structure

---

# Technologies Used

| Tool         | Purpose              |
| ------------ | -------------------- |
| Python       | Programming Language |
| Pandas       | Data Processing      |
| Scikit-learn | Machine Learning     |
| FastAPI      | API Development      |
| Evidently AI | Data Drift Detection |
| Joblib       | Model Saving         |
| Uvicorn      | FastAPI Server       |

---

# Project Architecture

```text
User Input
    ↓
Feature Validation Pipeline
    ↓
Validated Data
    ↓
Machine Learning Model
    ↓
Prediction Result
```

---

# Installation

## Clone the Repository

```bash
git clone <repository-url>
```

## Navigate to Project Folder

```bash
cd Depression_Model_Project
```

## Create Virtual Environment

```bash
python -m venv .venv
```

## Activate Virtual Environment

### Windows

```bash
.venv\Scripts\activate
```

### Linux / Mac

```bash
source .venv/bin/activate
```

---

# Install Dependencies

```bash
pip install -r requirements.txt
```

---

# Requirements

```text
pandas
scikit-learn
fastapi
uvicorn
joblib
pydantic
evidently
imbalanced-learn
```

---

# Dataset

The dataset contains features related to user behavior and lifestyle patterns.

### Example Features

* age
* gender
* daily_social_media_hours
* platform_usage
* sleep_hours

### Target Column

* depression

---

# Model Training

Run the following command to train the model:

```bash
python train_model.py
```

The trained model will be saved as:

```text
depression_model.pkl
```

---

# Feature Validation Pipeline

The validation pipeline checks:

* Missing values
* Invalid age values
* Negative feature values
* Invalid sleep hours
* Invalid categorical values

Validation is handled separately in:

```text
validation.py
```

---

# Data Drift Detection

Evidently AI is used to compare:

* Training data
* Current incoming data

Run:

```bash
python drift_detection.py
```

The generated report will be saved as:

```text
reports/drift_report.html
```

Open the HTML file in a browser to view:

* Feature drift
* Statistical comparison
* Data distribution changes
* Missing value analysis

---

# Run FastAPI Server

```bash
uvicorn app:app --reload
```

---

# API Documentation

After running FastAPI, open:

```text
http://127.0.0.1:8000/docs
```

Swagger UI will open automatically.

---

# Example Input

```json
{
  "age": 21,
  "gender": 1,
  "daily_social_media_hours": 6,
  "platform_usage": 2,
  "sleep_hours": 5
}
```

---

# Example Output

```json
{
  "prediction": "Depression Detected"
}
```

---

# Validation Error Example

```json
{
  "validation_errors": [
    "Invalid sleep hours found"
  ]
}
```

---

# Machine Learning Workflow

```text
Dataset
   ↓
Feature Validation
   ↓
Data Cleaning
   ↓
Train-Test Split
   ↓
Model Training
   ↓
Model Evaluation
   ↓
Data Drift Detection
   ↓
API Deployment
```

---

# Model Evaluation

The project evaluates the model using:

* Accuracy
* Precision
* Recall
* F1-score
* Classification Report

---

# Handling Class Imbalance

The project uses:

* SMOTE
* Class balancing techniques

to improve recall for minority depression cases.

---

# Future Improvements

* Streamlit Dashboard
* Docker Deployment
* Cloud Deployment
* MLflow Integration
* CI/CD Pipeline
* Real-Time Monitoring
* Database Integration

---

