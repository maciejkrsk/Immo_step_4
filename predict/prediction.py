import pickle
# import sklearn
from preprocessing.cleaning_data import preprocess

def predict(preprocessed_data):
   
    with open("model/model.pkl", "rb") as file:
        pickle_model = pickle.load(file)

    processed_data = preprocess(preprocessed_data)

    test_predict = pickle_model.predict(processed_data)

    return test_predict[0]


def predict_no_arguments():
    return (
        "To predict a price, it is necessary to provide house properties in json format"
    )
