from fastapi import FastAPI, HTTPException
from fastapi.responses import JSONResponse
from fastapi.middleware.cors import CORSMiddleware
from schema.input_value import UserInput
from model.predict import predict_car_price

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/")
def car_price_prediction():
    return {"message":"Car price. prediction"}

@app.post("/predict")
def predict_price(user_input: UserInput):
        brand = user_input.brand
        model_year = user_input.model_year
        milage = user_input.milage
        fuel_type = user_input.fuel_type
        engine_size = user_input.engine_size
        horsepower = user_input.horsepower
        cylinders = user_input.cylinders
        transmission = user_input.transmission
        accident = user_input.accident


        try: 

            price = predict_car_price(brand, model_year, milage, fuel_type, engine_size, horsepower, cylinders, transmission, accident)
 
            return JSONResponse(status_code= 200 , content={"price": round(price, 2)})
        except Exception as e:
             return HTTPException(status_code=400, detail=e)



