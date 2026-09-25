# Python Data Structures & Functions Demo

A beginner-friendly Python project demonstrating basic data structures and functions.

## Concepts Covered

- List
- Tuple
- Dictionary
- Key-Value Pairs
- Functions

## Features

### 1. List
Demonstrates creating a list and adding a new student using `append()`.

### 2. Tuple
Demonstrates creating a tuple and accessing its elements.

### 3. Dictionary
Stores student information using key-value pairs.

### 4. Key-Value Pairs
Uses a `for` loop with `.items()` to display dictionary keys and values.

### 5. Function
Uses a function to calculate the total of student marks.

## How to Run

Make sure Python is installed, then run:

```bash
python main.py
# Python Data Structures & Functions Demo

A beginner-friendly Python project demonstrating basic data structures, functions, and Python operators.

## Concepts Covered

* List
* Tuple
* Dictionary
* Key-Value Pairs
* Functions
* Arithmetic Operators
* Relational / Comparison Operators
* Assignment Operators
* Logical Operators
* Bitwise Operators
* Membership Operators
* Identity Operators
* Operator Precedence

## Project Files

### `main.py`

Demonstrates:

* List
* Tuple
* Dictionary
* Key-value pairs
* Functions

### `operators_demo.py`

Demonstrates different types of Python operators.

#### 1. Arithmetic Operators

```text
+    Addition
-    Subtraction
*    Multiplication
/    Division
//   Floor Division
%    Modulus
**   Exponent
```

#### 2. Relational / Comparison Operators

```text
==   Equal
!=   Not Equal
>    Greater Than
<    Less Than
>=   Greater Than or Equal
<=   Less Than or Equal
```

#### 3. Assignment Operators

```text
=    Assignment
+=   Add and Assign
-=   Subtract and Assign
*=   Multiply and Assign
/=   Divide and Assign
```

#### 4. Logical Operators

```text
and
or
not
```

#### 5. Bitwise Operators

```text
&    AND
|    OR
^    XOR
~    NOT
<<   Left Shift
>>   Right Shift
```

#### 6. Membership Operators

```text
in
not in
```

#### 7. Identity Operators

```text
is
is not
```

#### 8. Operator Precedence

Demonstrates the order in which Python evaluates expressions.

Example:

```python
10 + 5 * 2
```

Output:

```text
20
```

Multiplication is performed before addition.

## How to Run

Make sure Python is installed.

Run the main project:

```bash
python main.py
```

Run the operators demo:

```bash
python operators_demo.py
```

## Example Output

```text
ARITHMETIC OPERATORS
a + b = 13
a - b = 7
a * b = 30

RELATIONAL / COMPARISON OPERATORS
a == b : False
a != b : True
a > b  : True

LOGICAL OPERATORS
age > 18 and has_id : True

BITWISE OPERATORS
p & q  = 2
p | q  = 11
p ^ q  = 9
```
# NumPy Array Practice

## Array Creation

```python
from numpy import *

a = array([1, 2, 3], int)
print(a)

a = array([1.1, 2.2, 3.3], float)
print(a)

a = array(['a', 'b', 'c'])
print(a)
```

## Array Functions

```python
linspace(0, 10, 5)   # Evenly spaced values
logspace(1, 4, 5)    # Logarithmic values
arange(1, 10, 3)     # Values with step
zeros(5)              # Zeros
ones(5)               # Ones
```

## Array Attributes

```python
b = array([1, 2, 3, 4, 5])

b.ndim       # Dimensions
b.shape      # Shape
b.size       # Total elements
b.itemsize   # Size of one element
b.dtype      # Data type
b.nbytes      # Total memory
```

## Dimensions

```python
# 1D
a = array([1, 2, 3])

# 2D
b = array([[1, 2, 3], [4, 5, 6]])

# 3D
c = array([[[1, 2], [3, 4]], [[5, 6], [7, 8]]])
```

### Quick Notes

- `array()` → Create array
- `linspace()` → Equal spacing
- `logspace()` → Logarithmic spacing
- `arange()` → Range with step
- `zeros()` → Zeros
- `ones()` → Ones
- `ndim` → Number of dimensions
- `shape` → Rows and columns
- `size` → Number of elements
- `dtype` → Data type
## Purpose

This project is created for learning and practicing fundamental Python programming concepts and operators.

## Author

**Vidya Faldu**

MCA Student
Atmiya University
Rajkot, Gujarat
