import pickle

# import sklearn
from preprocessing.cleaning_data import preprocess


def predict(preprocessed_data):
    with open("model/model_final1.pkl", "rb") as file:
        pickle_model = pickle.load(file)

    processed_data = preprocess(preprocessed_data)

    test_predict = pickle_model.predict(processed_data)
    predicted_result = {"prediction": int(test_predict[0])}
    return predicted_result


def predict_no_arguments():
    return (
        "To predict a price, it is necessary to provide house properties in json format"
    )
