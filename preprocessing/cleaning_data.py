import pandas as pd
from fastapi import HTTPException


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
        "full_address",
        "swimming_pool",
        "open_fire",
        "terrace",
        "terrace_area",
        "facades_number",
        "building_state",
    ]

    df = df.drop(columns=to_remove)
    df.rename(columns={"property_type": "Subtype"}, inplace=True)
    df.rename(columns={"area": "Living area"}, inplace=True)
    df.rename(columns={"equipped_kitchen": "Kitchen type"}, inplace=True)
    df.rename(columns={"furnished": "Furnished"}, inplace=True)

    properties = ["HOUSE", "APARTMENT", "OTHERS"]
    if df["Subtype"].iloc[0] not in properties:
        raise HTTPException(
            status_code=500,
            detail="Please insert a valid property type : APARTMENT, HOUSE, OTHERS",
        )

    df = df[["Living area", "Subtype", "Furnished", "Kitchen type"]]
    df["Subtype"] = df["Subtype"].replace("HOUSE", 0, regex=True)
    df["Subtype"] = df["Subtype"].replace("OTHERS", 1, regex=True)
    df["Subtype"] = df["Subtype"].replace("APARTMENT", 2, regex=True)

    if df["Living area"].iloc[0] <= 15:
        raise HTTPException(
            status_code=500,
            detail="Number above 15 pls",
        )
    return df
