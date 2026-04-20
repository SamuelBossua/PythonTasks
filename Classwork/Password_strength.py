# 1. prompt user to enter a password

# 2. if the length of characters in the password is less than 8, print very weak

# 3. if the length of the password 8, print weak

# 4. if the legth of the password is between 8 & 16 , print strong

#5. if the password is graeter than 16, print strong












password = str(input("Enter a password: "))

if len(password) < 8:
 print("Strength: very weak")

elif len(password) == 8:
 print("Strength: weak")

elif len(password) >= 8 and len(password) <= 16:
 print("Strength: strong")

elif len(password) >= 16:
 print("Strength: very strong")