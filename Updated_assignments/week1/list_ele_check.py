# write a program to find whether the element exists in the list

# Function to check if an element exists in the list
def element_exists(lst, element):
    return element in lst

# Sample list
my_list = [1, 2, 3, 4, 5]

# Input element to check
element = int(input("Enter the element to check: "))

# Check if the element exists in the list
if element_exists(my_list, element):
    print(f"{element} exists in the list.")
else:
    print(f"{element} does not exist in the list.")

