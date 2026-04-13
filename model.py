import pandas as pd
from sklearn.linear_model import LinearRegression
import pickle

def train_model():
    data = pd.read_csv("finance_data.csv")
    
    X = data[["income", "expenses"]]
    y = data["savings"]
    
    model = LinearRegression()
    model.fit(X, y)
    
    with open("model.pkl", "wb") as f:
        pickle.dump(model, f)

def predict_savings(income, expenses):
    with open("model.pkl", "rb") as f:
        model = pickle.load(f)
    
    prediction = model.predict([[income, expenses]])
    return prediction[0]