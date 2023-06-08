from preprocessing.cleaning_data import preprocess
from predict.prediction import *
from fastapi import FastAPI, Request, HTTPException, status, APIRouter
from pydantic import BaseModel
from fastapi.responses import JSONResponse
from http import HTTPStatus
import pickle

app = FastAPI()
router = APIRouter()
with open("model/model.pkl", "rb") as file:
    pickle_model = pickle.load(file)
# result = loaded_model.score(X_test, Y_test)


@app.exception_handler(HTTPException)
def http_exception_handler(request: Request, exc: HTTPException):
    return JSONResponse(status_code=exc.status_code, content={"error": exc.detail})


class Data(BaseModel):
    area: int  # Living area
    property_type: str  # Subtype
    rooms_number: int | None = None  # Bedrooms
    zip_code: int  # Postcode
    land_area: int | None = None  # Dont have
    garden: bool | None = None  # Garden
    garden_area: int | None = None  # Garden surface
    equipped_kitchen: bool  # Kitchen type
    full_address: str | None = None  # Address
    swimming_pool: bool | None = None  # Swimming pool
    furnished: bool | None = None  # Furnished
    open_fire: bool | None = None  # How many fireplaces?
    terrace: bool | None = None  # Terrace
    terrace_area: int | None = None  # Terrace area
    facades_number: int | None = None  # Number of frontages
    building_state: str | None = None  # Building condition


@app.get("/")
def read_root():
    if HTTPStatus.OK == 200:
        return "Alive"


@app.post("/predict")
def prediction(properties_data: Data):
    return predict(properties_data)


@app.get("/predict")
def prediction():
    return predict_no_arguments()


# to run uvicorn immo_eliza_deploy:app --reload



