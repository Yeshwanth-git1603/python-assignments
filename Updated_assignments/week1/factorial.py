# write a program to find the factorial of a given number

# Function to calculate factorial
def factorial(n):
    if n == 0 or n == 1:
        return 1
    else:
        return n * factorial(n - 1)

# Input number
num = int(input("Enter a number: "))

# Check if the number is non-negative
if num < 0:
    print("Factorial is not defined for negative numbers.")
else:
    # Calling the factorial function and displaying the result
    print(f"The factorial of {num} is {factorial(num)}")

