# write a program to check whether a given number is even or odd
# Function to check if a number is even or odd
def check_even_odd(num):
    if num % 2 == 0:
        return "Even"
    else:
        return "Odd"

# Input a number
num = int(input("Enter a number: "))

# Check and display whether the number is even or odd
result = check_even_odd(num)
print(f"The number {num} is {result}.")

