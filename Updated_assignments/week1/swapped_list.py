#Given a list, write a Python program to swap first and last element of the list. 


# Function to swap the first and last element of a list
def swap_first_last(lst):
    if len(lst) < 2:
        return lst  # No need to swap if the list has less than 2 elements
    
    # Swapping the first and last element
    lst[0], lst[-1] = lst[-1], lst[0]
    
    return lst

# Sample list
my_list = [1, 2, 3, 4, 5]

# Swapping first and last element
swapped_list = swap_first_last(my_list)

# Display the modified list
print(f"List after swapping: {swapped_list}")
