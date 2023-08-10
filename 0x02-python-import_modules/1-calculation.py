from calculator_1 import add, sub, mul, div

# Assign values to variables a and b
a = 10
b = 5

# Import specific functions from calculator_1.py

# Call each of the imported functions
add_result = add(a, b)
subtract_result = sub(a, b)
multiply_result = mul(a, b)
divide_result = div(a, b)

# Print the results
print(f"{a} + {b} = {add_result}")
print(f"{a} - {b} = {subtract_result}")
print(f"{a} * {b} = {multiply_result}")
print(f"{a} / {b} =  {divide_result}")
