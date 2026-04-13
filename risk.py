def calculate_risk(income, expenses):
    ratio = expenses / income
    
    if ratio > 0.7:
        return "High Risk"
    elif ratio > 0.5:
        return "Medium Risk"
    else:
        return "Low Risk"