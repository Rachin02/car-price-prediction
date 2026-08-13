from pydantic import BaseModel, Field
from typing import Annotated, Literal


class UserInput(BaseModel):
    brand:Annotated[str, Field(description="brand name of the car", default="Ford")]
    model_year:Annotated[int, Field(description="Car launch year", default= 2024)]
    milage: Annotated[int, Field(description="Milage of the car", default= 51000)]
    fuel_type: Annotated[Literal['Other', 'Gasoline', 'Hybrid', 'Diesel'], Field(description="source of power.choose from = ['Other', 'Gasoline', 'Hybrid', 'Diesel'] ", default="Gasoline")]
    engine_size:Annotated[float, Field(description="size of the engine", default= 3.7)]
    horsepower: Annotated[float, Field(description="Horsepower of the engine", default= 600.0)]
    cylinders: Annotated[float, Field(description="total number of cylinders in the engine" , default=6)]
    transmission: Annotated[Literal['Automatic', 'Other', 'Manual', 'CVT'], Field(description="Transmission type", default="Manual")]
    accident: Annotated[Literal["No","Yes"], Field(description="Did any accident happen?", default= "No")]

