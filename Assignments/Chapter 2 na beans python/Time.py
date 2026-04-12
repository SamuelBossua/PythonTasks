number = int(input("Enter a number of seconds: "))
hours = number // 3600
remaining = number % 3600
minutes = remaining // 60
seconds = remaining % 60

print(hours, "hours(s)" , minutes , "minutes(s)" , seconds, "second(s)" ) 
