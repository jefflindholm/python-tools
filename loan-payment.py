def get_valid_float_input(prompt):
    while True:
        try:
            value = float(input(prompt))
            if value <= 0:
                print("Please enter a positive number.")
                continue
            return value
        except ValueError:
            print("Please enter a valid number.")

def get_valid_int_input(prompt):
    while True:
        try:
            value = int(input(prompt))
            if value <= 0:
                print("Please enter a positive number.")
                continue
            return value
        except ValueError:
            print("Please enter a valid number.")

def calculate_loan_payment(principal, annual_interest_rate, months):
    # Convert annual interest rate to monthly interest rate
    monthly_interest_rate = annual_interest_rate / 12 / 100
    
    # Calculate monthly payment using the loan payment formula
    if monthly_interest_rate == 0:
        monthly_payment = principal / months
    else:
        monthly_payment = principal * (monthly_interest_rate * (1 + monthly_interest_rate)**months) / ((1 + monthly_interest_rate)**months - 1)
    
    total_payment = monthly_payment * months
    return monthly_payment, total_payment

def main():
    print("Loan Payment Calculator")
    print("-" * 20)
    
    # Get loan details from user
    principal = get_valid_float_input("Enter the loan amount: $")
    annual_interest_rate = get_valid_float_input("Enter the annual interest rate (%): ")
    months = get_valid_int_input("Enter the loan term in months: ")
    
    # Calculate payments
    monthly_payment, total_payment = calculate_loan_payment(principal, annual_interest_rate, months)
    
    # Display results
    print("\nLoan Summary:")
    print(f"Principal Amount: ${principal:,.2f}")
    print(f"Annual Interest Rate: {annual_interest_rate:.2f}%")
    print(f"Loan Term: {months} months")
    print(f"Monthly Payment: ${monthly_payment:,.2f}")
    print(f"Total Payment: ${total_payment:,.2f}")
    print(f"Total Interest: ${(total_payment - principal):,.2f}")

if __name__ == "__main__":
    main()