import pickle

def save_model(model, scaler):

    with open("models/traffic_model.pkl","wb") as f:
        pickle.dump(model,f)

    with open("models/scaler.pkl","wb") as f:
        pickle.dump(scaler,f)