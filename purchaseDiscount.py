# 1. asks the user to enter the amont they have spent

# 2. if the amount is between 1000 and 10000 , discount = 5% off


purchase_amount = int(input("Enter an amount : "))

if purchase_amount >= 1000 and purchase_amount <= 10000:

 discount = purchase_amount - (0.05 * purchase_amount)
 print (discount)

elif purchase_amount >= 10000 and purchase_amount <= 50000:

 discount = purchase_amount - (0.1 * purchase_amount)
 print (discount)

elif purchase_amount > 500000:

  discount = purchase_amount - (0.2 * purchase_amount) 
  print (discount)

else: print("no discount")




