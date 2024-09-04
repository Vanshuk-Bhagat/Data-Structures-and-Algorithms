def insertion_sort(array):
    # Loop through each element starting from the second one (index 1)
    for i in range(1, len(array)):
        temp = array[i]  # Store the current element in temp
        j = i - 1  # Start by comparing the current element with the one just before it
        
        # Compare the temp with elements in the sorted portion (from right to left)
        while j >= 0 and temp < array[j]:  # If temp is smaller than array[j], shift array[j] to the right
            array[j + 1] = array[j]  # Shift the larger element to the right
            j = j - 1  # Move the index one step to the left to continue comparisons
        
        # Place the temp in its correct position
        array[j + 1] = temp  # Once the correct spot is found, insert the temp value there

    return array  # Return the sorted array


# Test the function with an example array
array = [2, 1, 4, 5, 0, 7, 6, 8]
insert = insertion_sort(array)
print(insert)
