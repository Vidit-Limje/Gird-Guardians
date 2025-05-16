import pandas as pd
from sklearn.ensemble import RandomForestClassifier
import joblib
from preprocess import preprocess_data

def train():
    # Example: Load your data here
    df = pd.read_csv('data.csv')
    X, y = preprocess_data(df)
    model = RandomForestClassifier()
    model.fit(X, y)
    joblib.dump(model, 'random_forest.pkl')

if __name__ == '__main__':
    train() 