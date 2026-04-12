principal = float(input("Enter a principal: "))
rate = float(input("Enter a rate (%): "))
time = float(input("Enter a number of years: "))

SI = (principal * rate * time)/100
amount = principal + SI

print("The simple interst is:" , SI)
print("The total amount is:" , amount)