#condition 
# Positive, negative or zero

number = int(input("enter number: "))

if number > 0:
    print("number is positive")
elif number < 0:
    print("number is negative")
else:
    print("number is zero")

# Check voting eligibility

age = int(input("enter age: "))
if age >= 18:
    print("person is eligible to vote")
else:
    print("person is not eligible to vote")

# Largest of three numbers

a = int(input("enter first number: "))
b = int(input("enter second number: "))
c = int(input("enter third number: "))

if a >= b and a >= c:
    print("largest number:", a)
elif b >= a and b >= c:
    print("largest number:", b)
else:
    print("largest number:", c)

# Check leap year
year = int(input("enter year: "))
if year % 400 == 0:
    print("leap year")
elif year % 100 == 0:
    print("not a leap year")
elif year % 4 == 0:
    print("leap year")
else:
    print("not a leap year")


# Grade system

marks = int(input("enter marks: "))

if marks >= 90:
    print("Grade A")
elif marks >= 80:
    print("Grade B")
elif marks >= 70:
    print("Grade C")
elif marks >= 60:
    print("Grade D")
elif marks >= 50:
    print("Grade E")
else:
    print("Fail")

# Divisible by 5 and 11
number = int(input("enter number: "))

if number % 5 == 0 and number % 11 == 0:
    print("number is divisible by 5 and 11")
else:
    print("number is not divisible by 5 and 11")

# Simple calculator

a = float(input("enter first number: "))
b = float(input("enter second number: "))

operator = input("enter operator (+, -, *, /): ")

if operator == "+":
    print("result:", a + b)
elif operator == "-":
    print("result:", a - b)
elif operator == "*":
    print("result:", a * b)
elif operator == "/":
    print("result:", a / b)
else:
    print("invalid operator")