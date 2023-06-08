import pandas as pd
from datetime import date
import numpy as np
from urllib.parse import unquote
from fastapi.responses import JSONResponse
from fastapi import FastAPI, Request, HTTPException, status, APIRouter


# If required not fulfilled, return error
# This file should contain a function called preprocess() that will take a new house's
# data as input and return those data preprocessed as output.
def preprocess(new_house):
    df = pd.DataFrame()
    new_house_dict = {item[0]: item[1] for item in new_house}
    for key in new_house_dict:
        temp = new_house_dict.get(key)
        df[key] = [temp]

    to_remove = [
        "rooms_number",
        "zip_code",
        "land_area",
        "garden",
        "garden_area",
        "equipped_kitchen",
        "full_address",
        "swimming_pool",
        "furnished",
        "open_fire",
        "terrace",
        "terrace_area",
        "facades_number",
        "building_state",
    ]

    df = df.drop(columns=to_remove)
    df.rename(columns={"property_type": "Subtype"}, inplace=True)
    df.rename(columns={"area": "Living area"}, inplace=True)
    # df["Subtype"]= df["property_type"] 
    df["Subtype"] = df["Subtype"].replace("HOUSE", 0, regex=True)
    df["Subtype"] = df["Subtype"].replace("OTHERS", 1, regex=True)
    df["Subtype"] = df["Subtype"].replace("APARTMENT", 2, regex=True)
  

    try:
        int(df["Subtype"])
    except ValueError:
        raise HTTPException(
            status_code=500,
            detail="Please insert a valid property type : APARTMENT, HOUSE, OTHER",
        )

    if df["Living area"].iloc[0] <= 15:
        raise HTTPException(
            status_code=500,
            detail="Number above 15 pls",
        )
    # print(df)

    


    return df