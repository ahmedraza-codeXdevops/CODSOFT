print("=" * 40)
print("      BUSINESS LOAN EMI CALCULATOR")
print("=" * 40)

# User Input
loan_amount = float(input("Enter Loan Amount (₹): "))
annual_interest = float(input("Enter Annual Interest Rate (%): "))
years = int(input("Enter Loan Tenure (Years): "))

# Convert to monthly values
monthly_interest = annual_interest / (12 * 100)
months = years * 12

# EMI Calculation
if monthly_interest == 0:
    emi = loan_amount / months
else:
    emi = (loan_amount * monthly_interest * (1 + monthly_interest) ** months) / ((1 + monthly_interest) ** months - 1)

total_payment = emi * months
total_interest = total_payment - loan_amount

# Display Results
print("\n" + "=" * 40)
print("          LOAN SUMMARY")
print("=" * 40)

print(f"Loan Amount      : ₹{loan_amount:.2f}")
print(f"Interest Rate    : {annual_interest}%")
print(f"Loan Tenure      : {years} Years")
print(f"Monthly EMI      : ₹{emi:.2f}")
print(f"Total Payment    : ₹{total_payment:.2f}")
print(f"Total Interest   : ₹{total_interest:.2f}")

print("=" * 40)
print("Thank you for using EMI Calculator!")