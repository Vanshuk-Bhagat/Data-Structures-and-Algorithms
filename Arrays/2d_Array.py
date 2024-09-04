# Prompt the user for the number of rows and columns
r_num = int(input("Input number of rows: "))
c_num = int(input("Input number of columns: "))

# Create a 2D array (list of lists) initialized with zeros
twod_arr = [[0 for col in range(c_num)] for row in range(r_num)]

# Fill the 2D array with the product of the row and column indices
for row in range(r_num):
    for col in range(c_num):
        twod_arr[row][col] = row * col

# Print the 2D array
print(twod_arr)
