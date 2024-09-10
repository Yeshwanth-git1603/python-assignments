#Write a program to check whether a given number is prime or not 

# Function to check if a number is prime
def is_prime(num):
    # A prime number is greater than 1
    if num <= 1:
        return False
    # Check from 2 to the square root of num
    for i in range(2, int(num**0.5) + 1):
        if num % i == 0:
            return False
    return True

# Input a number
num = int(input("Enter a number: "))

# Check and display whether the number is prime or not
if is_prime(num):
    print(f"{num} is a prime number.")
else:
    print(f"{num} is not a prime number.")

