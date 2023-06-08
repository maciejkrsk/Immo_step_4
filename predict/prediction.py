def predict(preprocessed_data):
    import pickle
    import pandas as pd
    from preprocessing.cleaning_data import preprocess

    # All the code to predict a price
    with open("model/model.pkl", "rb") as file:
        pickle_model = pickle.load(file)

    processed_data = preprocess(preprocessed_data)

    test_predict = pickle_model.predict(processed_data)

    return test_predict[0]


def predict_no_arguments():
    return (
        "To predict a price, it is necessary to provide house properties in json format"
    )
