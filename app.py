from predict.prediction import predict, predict_no_arguments
from fastapi import FastAPI, Request, HTTPException, APIRouter
from pydantic import BaseModel
from fastapi.responses import JSONResponse
from http import HTTPStatus


app = FastAPI()
router = APIRouter()


@app.exception_handler(HTTPException)
def http_exception_handler(request: Request, exc: HTTPException):
    return JSONResponse(status_code=exc.status_code, content={"error": exc.detail})


class Data(BaseModel):
    area: int
    property_type: str
    rooms_number: int | None = None
    zip_code: int
    land_area: int | None = None
    garden: bool | None = None
    garden_area: int | None = None
    equipped_kitchen: bool
    full_address: str | None = None
    swimming_pool: bool | None = None
    furnished: bool
    open_fire: bool | None = None
    terrace: bool | None = None
    terrace_area: int | None = None
    facades_number: int | None = None
    building_state: str | None = None


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
