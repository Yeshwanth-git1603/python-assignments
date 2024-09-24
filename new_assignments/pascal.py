def print_pascals_triangle(n):
    if n <= 0:
        return
    
    triangle = []
    
    for row in range(n):
        # Start a new row
        new_row = [1] * (row + 1)
        
        # Calculate the values for the inner elements of the row
        for j in range(1, row):
            new_row[j] = triangle[row - 1][j - 1] + triangle[row - 1][j]
        
        # Append the new row to the triangle
        triangle.append(new_row)

        # Print the current row
        print(' '.join(map(str, new_row)).center(n * 2))

print_pascals_triangle(5)
