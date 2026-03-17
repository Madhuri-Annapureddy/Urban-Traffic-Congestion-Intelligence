import pickle
import numpy as np

def load_model():

    model = pickle.load(open("models/traffic_model.pkl","rb"))
    scaler = pickle.load(open("models/scaler.pkl","rb"))

    return model, scaler


def predict(input_data):

    model, scaler = load_model()

    data = np.array(input_data).reshape(1,-1)
    data = scaler.transform(data)

    prediction = model.predict(data)

    return prediction[0]