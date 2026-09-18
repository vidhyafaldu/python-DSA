#operator
# Arithmetic operators

a = 20
b = 10

addition = a + b
subtraction = a - b
multiplication = a * b
division = a / b

print("addition:", addition)
print("subtraction:", subtraction)
print("multiplication:", multiplication)
print("division:", division)

# Remainder and quotient

a = 25
b = 4

remainder = a % b
quotient = a // b

print("remainder:", remainder)
print("quotient:", quotient)

# Check even or odd

number = int(input("enter number: "))

if number % 2 == 0:
    print("number is even")
else:
    print("number is odd")


# Relational operators

a = 10
b = 20
print("a == b:", a == b)
print("a != b:", a != b)
print("a > b:", a > b)
print("a < b:", a < b)
print("a >= b:", a >= b)
print("a <= b:", a <= b)

# Logical operators

a = 10
b = 20

print("and:", a < 20 and b > 10)
print("or:", a > 20 or b > 10)
print("not:", not(a > b))

# Assignment operators

a = 10
print("before:", a)
a += 5
print("after +=:", a)
a -= 2
print("after -=:", a)
a *= 2
print("after *=:", a)
a /= 2
print("after /=:", a)

# Find largest number

a = int(input("enter first number: "))
b = int(input("enter second number: "))
if a > b:
    print("largest number:", a)
else:
    print("largest number:", b)