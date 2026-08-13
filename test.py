from model.predict import predict_car_price

price = predict_car_price("BMW", 2024, 51000,"Gasoline",3.7,600.0,6,"Manual","NO")
print(price)