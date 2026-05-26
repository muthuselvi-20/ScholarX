# Build a feature validation pipeline
## Project Overview

- This project is a Machine Learning based Depression Prediction System integrated with a Feature Validation Pipeline and Data Drift Detection.
- The system validates incoming user data before sending it to the trained model for prediction. This helps improve model reliability and prevents incorrect predictions caused by invalid or poor-quality data.
- The project also uses Evidently AI for monitoring and detecting data drift between training data and new incoming data.

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

# Requirements

```text
pandas
scikit-learn
fastapi
uvicorn
joblib
pydantic
evidently
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
validate.py
```

---

# Data Drift Detection

Evidently AI is used to compare:

* Training data
* Current incoming data

Run:

```bash
python data_drift.py
```

The generated report will be saved as:

```text
data_drift_report.html
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
<img width="1920" height="1020" alt="Screenshot 2026-05-26 145615" src="https://github.com/user-attachments/assets/302da36c-4cc1-484d-b4ba-3ecbab287383" />

---

# API Documentation

After running FastAPI, open:

```text
http://127.0.0.1:8000/docs
```

Swagger UI will open automatically.

---

# Example Input [without error]

<img width="1854" height="540" alt="Screenshot 2026-05-26 150438" src="https://github.com/user-attachments/assets/98e3368e-d30b-488b-a886-a721574db9d3" />

---
# Example Output [without error]

<img width="1134" height="131" alt="Screenshot 2026-05-26 150448" src="https://github.com/user-attachments/assets/9b92a3a6-900c-4854-b888-b65f288588c0" />

---
# Example Input [with error]

<img width="1738" height="475" alt="Screenshot 2026-05-26 155141" src="https://github.com/user-attachments/assets/3892c440-6fc8-409c-8ca6-bec30a9bf7e0" />

---
# Validation Error Example

<img width="1681" height="204" alt="Screenshot 2026-05-26 155203" src="https://github.com/user-attachments/assets/3ed0e5b3-3870-4c46-834d-754058a3ae30" />


---
# Data drift Report [Evidently Ai]

<img width="1920" height="1020" alt="Screenshot 2026-05-26 160033" src="https://github.com/user-attachments/assets/3f32b771-9b5d-4968-bab8-4a81e62cd959" />

---

<img width="1920" height="1020" alt="Screenshot 2026-05-26 160013" src="https://github.com/user-attachments/assets/c28c783a-f73a-4eff-b47f-ce1203239532" />

---
