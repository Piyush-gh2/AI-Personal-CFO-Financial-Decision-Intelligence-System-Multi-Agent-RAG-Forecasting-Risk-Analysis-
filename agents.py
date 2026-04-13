from src.model import predict_savings
from src.risk import calculate_risk

def financial_decision(income, expenses):
    
    predicted_savings = predict_savings(income, expenses)
    risk = calculate_risk(income, expenses)
    
    if risk == "Low Risk":
        advice = "You can invest more for higher returns."
    elif risk == "Medium Risk":
        advice = "Maintain balanced spending and savings."
    else:
        advice = "Reduce expenses and increase savings."
    
    return predicted_savings, risk, advice