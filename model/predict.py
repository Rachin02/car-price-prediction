import pickle
import pandas as pd
import numpy as np

with open("model.pkl", "rb") as f:
    m = pickle.load(f)

with open("scaler.pkl", "rb") as f:
    scaler = pickle.load(f)

with open("feature_columns.pkl", "rb") as f:
    feature_columns = pickle.load(f)


def simplify_brand(x):
    economy = ['Ford', 'Toyota', 'Chevrolet', 'Nissan','Honda', 'Hyundai', 'Kia', 'Mazda']
    luxury = ['BMW', 'Mercedes-Benz', 'Audi', 'Lexus', 'Acura']
    exotic = ['Porsche', 'Ferrari', 'Lamborghini','Bentley', 'Rolls-Royce', 'McLaren']
    electric = ['Tesla', 'Rivian', 'Lucid']

    if x in economy:
        return 'Economy'
    elif x in luxury:
        return 'Luxury'
    elif x in exotic:
        return 'Exotic'
    elif x in electric:
        return 'Electric'
    else:
        return 'Other'


def predict_car_price(brand, model_year, milage, fuel_type, engine_size, horsepower, cylinders, transmission, ext_col, int_col, accident):


    # Create dataframe
    car = pd.DataFrame([{
        'milage': milage,
        'accident': accident,
        'brand': brand,
        'model_year': model_year,
        'fuel_type': fuel_type,
        'engine_size': engine_size,
        'horsepower': horsepower,
        'cylinders': cylinders,
        'transmission': transmission,
        'ext_col': ext_col,
        'int_col': int_col,
        
    }])


    car['car_age'] = 2026 - car['model_year']

    # Brand group
    car['brand_group'] = car['brand'].apply(simplify_brand)


    # Accident
    if accident == 'No':
        car['accident'] = 0
    else:
        car['accident'] = 1


    # Remove unused columns
    car.drop( columns=[ 'model_year', 'brand'], inplace=True )


    # One-hot encoding
    cat_cols = ['fuel_type', 'transmission', 'brand_group' ]
    car = pd.get_dummies( car, columns=cat_cols, drop_first=True )

    # X_train columns from your training data
    car = car.reindex(
        columns= feature_columns,
        fill_value=False
    )


    # Scale numerical columns
    num_cols = [ 'milage', 'horsepower', 'engine_size', 'cylinders', 'car_age' ]
    car[num_cols] = scaler.transform( car[num_cols] )


    # Predict
    log_price = m.predict(car)[0]

    # Reverse log1p
    price = np.expm1(log_price)

    return price

price = predict_car_price(
    brand="Ford",
    model_year=2024,
    milage=51000,
    fuel_type="Gasoline",
    engine_size = 3.7,
    horsepower = 600.0,
    cylinders = 6,
    transmission="Manual",
    ext_col="Black",
    int_col="Black",
    accident="No"
)

print(f"Predicted car price: ${price:,.2f}")