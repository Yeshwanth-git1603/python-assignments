# write a program to delete an element in the list


# Function to delete an item by its value
def delete_by_value(lst, value):
    if value in lst:
        lst.remove(value)
        return True
    else:
        return False

# Sample list
my_list = [1, 2, 3, 4, 5]

# Input value to delete
value = int(input("Enter the value to delete: "))

# Delete the value and check if successful
if delete_by_value(my_list, value):
    print(f"Value {value} has been deleted.")
else:
    print(f"Value {value} not found in the list.")

# Display the modified list
print(f"List after deletion: {my_list}")
