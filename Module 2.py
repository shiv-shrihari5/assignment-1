# Get input from user and convert to integers
A = int(input("Enter the first number: "))
B = int(input("Enter the second number: "))

# Perform operations
print("Addition:", A + B)
print("Subtraction:", A - B)
print("Multiplication:", A * B)

# Handle division safely
if B != 0:
    print("Division:", A / B)
else:
    print("Division: Cannot divide by zero")
