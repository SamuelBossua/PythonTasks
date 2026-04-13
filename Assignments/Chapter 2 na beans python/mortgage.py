principal = float(input("Enter the principal (loan amount): "))
rate = float(input("Enter the monthly interest rate : "))
n = int(input("Enter number of payments (in months): "))

Mortgage = principal * (rate * (1 + rate) ** n) / ((1 + rate) ** n - 1)

print("Monthly payment is:", Mortgage)