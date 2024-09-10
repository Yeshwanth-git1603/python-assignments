# write a python program to filter positive elements in a list
# Function to filter positive numbers from the list
def filter_positive_numbers(lst):
    # Use list comprehension to filter positive numbers
    return [num for num in lst if num > 0]

# Sample list
my_list = [-10, 20, -30, 40, 0, 50, -60]

# Filtering positive numbers
positive_numbers = filter_positive_numbers(my_list)

# Display the positive numbers
print(f"Positive numbers in the list: {positive_numbers}")

