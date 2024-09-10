# write a program to remove the odd numbersin the list

# Function to remove all odd numbers from the list
def remove_odd_numbers(lst):
    # Use list comprehension to filter out odd numbers
    return [num for num in lst if num % 2 == 0]

# Sample list
my_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

# Remove odd numbers
filtered_list = remove_odd_numbers(my_list)

# Display the modified list
print(f"List after removing odd numbers: {filtered_list}")

