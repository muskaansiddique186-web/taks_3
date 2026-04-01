import math

# Step 1: Ask the user for a number
num = float(input("Enter a number: "))

# Step 2: Use the math module to calculate
sqrt_val = math.sqrt(num)
log_val = math.log(num)
sin_val = math.sin(num)

# Step 3: Display the results
print(f"Square root of {num} = {sqrt_val}")
print(f"Natural logarithm of {num} = {log_val}")
print(f"Sine of {num} (in radians) = {sin_val}")