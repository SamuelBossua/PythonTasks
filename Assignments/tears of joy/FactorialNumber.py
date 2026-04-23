#factorial

number = int(input("Enter a number: "))

count = 0
result = number


while count <= number:
 number = number - 1
 result = result * number
 count = count +1
print(result)