# write a program to swap the elements at the given positions

# Function to swap elements at given positions
def swap_elements(lst, pos1, pos2):
    # Swap the elements at pos1 and pos2
    lst[pos1], lst[pos2] = lst[pos2], lst[pos1]
    return lst

# Sample list
my_list = [10, 20, 30, 40, 50]

# Input positions to swap (1-based index for user input, convert to 0-based index)
pos1 = int(input("Enter the first position to swap: ")) - 1
pos2 = int(input("Enter the second position to swap: ")) - 1

# Swapping elements
swapped_list = swap_elements(my_list, pos1, pos2)

# Display the modified list
print(f"List after swapping: {swapped_list}")

