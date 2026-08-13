# 🚗 Used Car Price Prediction

An end-to-end **Machine Learning application for used car price prediction**, featuring a trained machine learning model, a **FastAPI REST API**, and a responsive **HTML/CSS frontend**.

The project takes vehicle specifications such as brand, model year, mileage, fuel type, engine size, horsepower, cylinders, transmission, and accident history, and predicts the estimated market price of the vehicle.

### 🌐 Live Project

**Live :**
https://car-price-prediction-lrcy.onrender.com/

> The backend API is deployed on an AWS instance and provides the prediction service consumed by the frontend.

---

## 📌 Project Overview

This project demonstrates the complete workflow of deploying a machine learning model as a real-world web application.

The workflow is:

```text
User
  │
  ▼
HTML / CSS Frontend
  │
  │  Vehicle Information
  ▼
FastAPI REST API
  │
  ▼
ML Prediction Pipeline
  │
  ▼
Trained Car Price Prediction Model
  │
  ▼
Predicted Car Price
  │
  ▼
Frontend
```

The frontend collects vehicle information and sends it to the FastAPI backend through an HTTP `POST` request. The backend processes the input using the trained machine learning model and returns the predicted car price in JSON format.

---

## ✨ Features

* 🚗 Used car price prediction
* 🤖 Machine learning-based prediction
* ⚡ FastAPI REST API
* 🌐 Interactive web interface
* 🎨 Custom HTML/CSS frontend
* 🔄 Frontend-to-backend API communication
* ☁️ Backend deployed on AWS
* 📦 Serialized machine learning model
* 📊 Input validation using Pydantic
* 💰 Price prediction rounded to two decimal places
* 📖 Automatic FastAPI API documentation

---

## 🧠 Machine Learning Model

The core of this project is a machine learning model trained to predict used car prices.

The trained model and supporting preprocessing objects are stored as serialized files:

```text
model.pkl
scaler.pkl
feature_columns.pkl
```

The prediction pipeline receives the following vehicle features:

| Feature        | Description                |
| -------------- | -------------------------- |
| `brand`        | Car manufacturer/brand     |
| `model_year`   | Manufacturing/model year   |
| `milage`       | Vehicle mileage            |
| `fuel_type`    | Fuel type                  |
| `engine_size`  | Engine size in liters      |
| `horsepower`   | Engine horsepower          |
| `cylinders`    | Number of engine cylinders |
| `transmission` | Transmission type          |
| `accident`     | Previous accident history  |

The prediction logic is implemented in:

```text
model/predict.py
```

---

## 🛠️ Technology Stack

### Machine Learning

* Python
* Scikit-learn
* Pandas
* NumPy
* Pickle

### Backend

* FastAPI
* Pydantic
* Uvicorn
* Python

### Frontend

* HTML5
* CSS3
* JavaScript
* Fetch API

### Deployment

* Docker
* AWS EC2
* REST API

---

## 📂 Project Structure

```text
CAR PRICE PREDICTION/
│
├── car/
│
├── frontend/
│   ├── index.html
│   ├── style.css
│   └── streamlit_version.py
│
├── model/
│   ├── predict.py
│   └── Used_car_price_prediction.ipynb
│
├── schema/
│   └── input_value.py
│
├── .dockerignore
├── .gitignore
├── app.py
├── Dockerfile
├── feature_columns.pkl
├── model.pkl
├── requirements.txt
├── scaler.pkl
└── test.py
```

---

## 🔄 How It Works

### 1. User Input

The user enters vehicle information through the web interface.

The frontend accepts:

* Car brand
* Model year
* Mileage
* Fuel type
* Engine size
* Horsepower
* Cylinders
* Transmission
* Previous accident history

## The frontend form and input fields are implemented in `frontend/index.html`.

### 2. API Request

After the user clicks **Predict Car Price**, JavaScript collects the form data and sends it to the FastAPI backend using a `POST` request.

```javascript
const response = await fetch(API_URL, {
    method: "POST",
    headers: {
        "Content-Type": "application/json"
    },
    body: JSON.stringify(data)
});
```

## The frontend then receives the prediction from the API and displays it to the user.

### 3. FastAPI Backend

The FastAPI backend defines a `/predict` endpoint that accepts the user's vehicle information.

```python
@app.post("/predict")
def predict_price(user_input: UserInput):
```

The input values are extracted and passed to the prediction function:

```python
price = predict_car_price(
    brand,
    model_year,
    milage,
    fuel_type,
    engine_size,
    horsepower,
    cylinders,
    transmission,
    accident
)
```

The API returns the predicted price as JSON:

```json
{
    "price": 24500.50
}
```

---

### 4. Model Prediction

The prediction logic is handled by:

```text
model/predict.py
```

The serialized model, scaler, and feature-column information are used to prepare the input and generate the final prediction.

---

### 5. Result

The predicted price is returned to the frontend and displayed in the prediction card.

Example:

```text
Estimated Car Price

$24,500.50
```

## 🔌 API Endpoint

### `POST /predict`

Predicts the estimated price of a used car.

#### Request

```json
{
    "brand": "Ford",
    "model_year": 2024,
    "milage": 51000,
    "fuel_type": "Gasoline",
    "engine_size": 3.7,
    "horsepower": 600,
    "cylinders": 6,
    "transmission": "Automatic",
    "accident": "No"
}
```

#### Response

```json
{
    "price": 24500.50
}
```

---

## 🐳 Docker

The project also includes a `Dockerfile` for containerizing the FastAPI application.

Build the Docker image:

```bash
docker build -t car-price-prediction .
```

Run the container:

```bash
docker run -p 8000:8000 car-price-prediction
```

The API can then be accessed at:

```text
http://localhost:8000
```

---

## ☁️ Deployment

The FastAPI backend has been containerized using Docker and deployed on an **AWS instance**.

Deployment architecture:

```text
GitHub Repository
       │
       ▼
Docker Image
       │
       ▼
AWS EC2 Instance
       │
       ▼
FastAPI Application
       │
       ▼
REST API
       │
       ▼
HTML/CSS Frontend
```

The frontend communicates with the deployed API through an HTTP request. The API endpoint is configured in the frontend JavaScript.

---

## 🎨 Frontend

The frontend is built using:

* HTML
* CSS
* JavaScript

It provides a simple interface where users can enter their vehicle specifications and receive an estimated price.

The interface includes:

* Vehicle information form
* Prediction button
* Loading state
* Prediction result card
* Error message handling

The page also includes a dedicated loading state while the API processes the request.

---

## 🧪 Testing

The project contains:

```text
test.py
```

which can be used to test the prediction/API functionality.

For API testing, you can also use:

* FastAPI Swagger UI
* Postman
* cURL
* Python requests

---

## 📊 Example Prediction Workflow

```text
Input
│
├── Brand: Ford
├── Model Year: 2024
├── Mileage: 51,000
├── Fuel Type: Gasoline
├── Engine Size: 3.7 L
├── Horsepower: 600
├── Cylinders: 6
├── Transmission: Automatic
└── Accident: No
        │
        ▼
    FastAPI API
        │
        ▼
   ML Prediction
        │
        ▼
 Estimated Price
```

---

## 📁 Important Files

| File                                    | Purpose                                  |
| --------------------------------------- | ---------------------------------------- |
| `app.py`                                | FastAPI application and API endpoints    |
| `model/predict.py`                      | Loads the model and performs predictions |
| `model/Used_car_price_prediction.ipynb` | Machine learning model development       |
| `schema/input_value.py`                 | Defines and validates API input          |
| `frontend/index.html`                   | Frontend user interface                  |
| `frontend/style.css`                    | Frontend styling                         |
| `model.pkl`                             | Trained machine learning model           |
| `scaler.pkl`                            | Feature preprocessing/scaling object     |
| `feature_columns.pkl`                   | Model feature information                |
| `requirements.txt`                      | Python dependencies                      |
| `Dockerfile`                            | Docker configuration                     |
| `test.py`                               | Testing script                           |

---

## 🔐 API Security Note

The current frontend communicates directly with the prediction API. For a production deployment, additional security measures can be considered, such as:

* Restricting CORS origins
* API authentication
* HTTPS
* Rate limiting
* Request validation
* Reverse proxy configuration
* Environment variables for configuration

---

## 🚧 Future Improvements

* [ ] Add user authentication
* [ ] Improve model accuracy with additional features
* [ ] Add model performance metrics
* [ ] Add prediction history
* [ ] Add database integration
* [ ] Add API authentication
* [ ] Configure production CORS settings
* [ ] Add automated CI/CD deployment
* [ ] Deploy the frontend separately
* [ ] Add monitoring and logging

---

## 👨‍💻 Author

**Nure Alam Siddiki Rachin**

This project was developed to demonstrate an end-to-end machine learning deployment workflow — from model development to API development, frontend integration, Docker containerization, and AWS deployment.

---

## ⭐ If You Like This Project

If you find this project useful or interesting, consider giving the repository a ⭐ on GitHub!
