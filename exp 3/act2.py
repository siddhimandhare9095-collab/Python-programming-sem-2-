def calculate_emi(principal, annual_rate, years):
    # Convert annual rate to monthly rate
    monthly_rate = annual_rate / (12 * 100)
    
    # Total number of monthly payments
    months = years * 12
    
    # EMI formula
    emi = (principal * monthly_rate * (1 + monthly_rate) ** months) / ((1 + monthly_rate) ** months - 1)
    
    return emi


# Example usage
loan_amount = 500000   # ₹5,00,000
rate = 7.5             # 7.5% annual interest
time = 5               # 5 years

emi = calculate_emi(loan_amount, rate, time)
print("Monthly EMI: ₹", round(emi, 2))
