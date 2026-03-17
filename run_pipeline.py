from src.data_loader import load_data
from src.preprocessing import preprocess_data
from src.feature_engineering import create_time_features, select_features
from src.train_model import train_models
from src.evaluate_model import evaluate_model
from src.utils import save_model

def main():

    df = load_data("data/raw/traffic.csv")

    df = create_time_features(df)

    df, encoders = preprocess_data(df)

    X, y = select_features(df)

    models, scaler, X_test, y_test = train_models(X,y)

    best_model = None
    best_score = -999

    for name, model in models.items():

        metrics = evaluate_model(model,X_test,y_test)

        print(name, metrics)

        if metrics["R2"] > best_score:
            best_score = metrics["R2"]
            best_model = model

    save_model(best_model, scaler)

if __name__ == "__main__":
    main()