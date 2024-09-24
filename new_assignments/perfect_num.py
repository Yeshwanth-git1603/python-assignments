# perferct number program
def is_perfect(n):
    if n <= 1:
        return False
    
    # Calculate the sum of proper divisors
    sum_of_divisors = 0
    for i in range(1, n // 2 + 1):
        if n % i == 0:
            sum_of_divisors += i
    
    # Check if the sum of divisors equals the number
    return sum_of_divisors == n

# Example usage
number = 28
if is_perfect(number):
    print(f"{number} is a perfect number.")
else:
    print(f"{number} is not a perfect number.")

"""
