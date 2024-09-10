# write a program to add only even numbers into the tuple

# Initialize an empty list to collect even numbers
even_numbers = []

# Loop through numbers from 1 to 20
for num in range(1, 21):
    if num % 2 == 0:
        even_numbers.append(num)

# Convert the list to a tuple
even_numbers_tuple = tuple(even_numbers)

# Display the tuple
print(f"Tuple with even numbers from 1 to 20: {even_numbers_tuple}")
