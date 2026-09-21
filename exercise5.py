#loops
# Print numbers from 1 to 10

for i in range(1, 11):
    print(i)

# Print numbers from 10 to 1

i = 10
while i >= 1:
    print(i)
    i = i - 1


# Multiplication table

number = int(input("enter number: "))
for i in range(1, 11):
    print(number, "x", i, "=", number * i)

# Sum from 1 to n

n = int(input("enter n: "))
sum = 0
for i in range(1, n + 1):
    sum = sum + i
print("sum:", sum)


# Factorial of a number

number = int(input("enter number: "))
factorial = 1
for i in range(1, number + 1):
    factorial = factorial * i

print("factorial:", factorial)

# Even numbers from 1 to 100

for i in range(1, 101):
    if i % 2 == 0:
        print(i)

# Reverse a number

number = int(input("enter number: "))

reverse = 0

while number > 0:
    digit = number % 10
    reverse = reverse * 10 + digit
    number = number // 10

print("reverse:", reverse)

# Count digits

number = int(input("enter number: "))

count = 0

while number > 0:
    number = number // 10
    count = count + 1

print("number of digits:", count)

# Check prime number

number = int(input("enter number: "))

count = 0

for i in range(1, number + 1):
    if number % i == 0:
        count = count + 1

if count == 2:
    print("prime number")
else:
    print("not a prime number")

# Fibonacci series

n = int(input("enter number of terms: "))
a = 0
b = 1
for i in range(n):
    print(a)
    c = a + b
    a = b
    b = c