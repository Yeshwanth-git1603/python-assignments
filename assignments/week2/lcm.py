# finding the lcm of two positive integers

def gcd(a, b):
    while b:
        a, b = b, a % b
    return a

# Function to calculate LCM of two numbers
def lcm(a, b):
    return abs(a * b) // gcd(a, b)


num1 = int(input("Enter the first number: "))
num2 = int(input("Enter the second number: "))

result = lcm(num1, num2)
print(f"The LCM of {num1} and {num2} is: {result}")


