# Python Operators Demo

a = 10
b = 3
print(" ARITHMETIC OPERATORS  ")

print("a + b =", a + b)    # Addition
print("a - b =", a - b)    # Subtraction
print("a * b =", a * b)    # Multiplication
print("a / b =", a / b)    # Division
print("a // b =", a // b)  # Floor Division
print("a % b =", a % b)    # Modulus
print("a ** b =", a ** b)  # Exponent


print("\n RELATIONAL / COMPARISON OPERATORS  ")

print("a == b :", a == b)  # Equal
print("a != b :", a != b)  # Not equal
print("a > b  :", a > b)   # Greater than
print("a < b  :", a < b)   # Less than
print("a >= b :", a >= b)  # Greater than or equal
print("a <= b :", a <= b)  # Less than or equal

print("\n  ASSIGNMENT OPERATORS  ")
x = 10
print("x =", x)
x += 5
print("x += 5 :", x)
x -= 2
print("x -= 2 :", x)
x *= 2
print("x *= 2 :", x)
x /= 2
print("x /= 2 :", x)

print("\n LOGICAL OPERATORS  ")
age = 22
has_id = True
print("age > 18 and has_id :", age > 18 and has_id)
print("age < 18 or has_id   :", age < 18 or has_id)
print("not has_id           :", not has_id)

print("\n BITWISE OPERATORS  ")
p = 10
q = 3
print("p & q  =", p & q)   # AND
print("p | q  =", p | q)   # OR
print("p ^ q  =", p ^ q)   # XOR
print("~p     =", ~p)      # NOT
print("p << 1 =", p << 1)  # Left shift
print("p >> 1 =", p >> 1)  # Right shift

print("\n  MEMBERSHIP OPERATORS  ")
students = ["Vidya", "Riya", "Neha"]
print("'Vidya' in students     :", "Vidya" in students)
print("'Aisha' in students     :", "Aisha" in students)
print("'Aisha' not in students:", "Aisha" not in students)

print("\n IDENTITY OPERATORS ")

list1 = [1, 2, 3]
list2 = list1
list3 = [1, 2, 3]
print("list1 is list2 :", list1 is list2)
print("list1 is list3 :", list1 is list3)
print("list1 == list3 :", list1 == list3)


print("\n OPERATOR PRECEDENCE  ")
result = 10 + 5 * 2
print("10 + 5 * 2 =", result)
