# Exercise 3_1

# Write a program to prompt the user for hours and rate per hour using raw_input to compute gross pay. Pay
# the hourly rate for the hours up to 40 and 1.5 times the hourly rate for all hours worked above 40 hours.
# Use 45 hours and a rate of 10.50 per hour to test the program (the pay should be 498.75). You should use
# raw_input to read a string and float() to convert the string to a number. Do not worry about error checking
# the user input - assume the user types numbers properly.

# prompt for hours and hourly rate, then convert to float

hrs = raw_input("Enter Hours: ")
h = float(hrs)
rate = raw_input("Enter Hourly Rate: ")
r = float(rate)

# pay hourly rate up to 40 hours

if h <= 40:
    pay = h * r
    
# pay 1.5 times hourly rate for hours greater than 40

else :
    pay = r * 40 + ( (h - 40) * 1.5 * r)
    
print pay