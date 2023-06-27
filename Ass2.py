# Arithmetic Operators
a = 10
b = 5
print(a + b)    # Addition operator: 15
print(a - b)    # Subtraction operator: 5
print(a * b)    # Multiplication operator: 50
print(a / b)    # Division operator: 2.0
print(a % b)    # Modulus operator: 0
print(a ** b)   # Exponent operator: 100000

# Comparison Operators
s1 = "hello"
s2 = "world"
print(s1 == s2)     # Equality operator: False
print(s1 != s2)     # Inequality operator: True
print(a > b)        # Greater than operator: True
print(a < b)        # Less than operator: False
print(a >= b)       # Greater than or equal to operator: True
print(a <= b)       # Less than or equal to operator: False

# Assignment Operators
c = 20
c += a      # Addition assignment operator: c = c + a = 30
c -= b      # Subtraction assignment operator: c = c - b = 25
c *= a      # Multiplication assignment operator: c = c * a = 250
c /= a      # Division assignment operator: c = c / a = 25.0
c %= b      # Modulus assignment operator: c = c % b = 0.0
c **= b     # Exponent assignment operator: c = c ** b = 0.0

# Logical Operators
d = True
e = False
print(d and e)      # Logical AND operator: False
print(d or e)       # Logical OR operator: True
print(not d)        # Logical NOT operator: False

# Bitwise Operators
f = 25
g = 15
print(f & g)        # Bitwise AND operator: 9
print(f | g)        # Bitwise OR operator: 31
print(f ^ g)        # Bitwise XOR operator: 22
print(~f)           # Bitwise NOT operator: -26
print(f << 2)       # Bitwise left shift operator: 100
print(f >> 2)       # Bitwise right shift operator: 6

# Identity Operators
h = 10
i = 10
print(h is i)       # Identity equality operator: True
print(h is not i)   # Identity inequality operator: False

# Membership Operators
j = [1, 2, 3, 4, 5]
print(3 in j)       # Membership operator: True
print(6 not in j)   # Membership operator: True
