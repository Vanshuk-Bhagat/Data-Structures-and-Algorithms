def quick_sort(array, low, high):
    if low < high: 
        # Get the pivot index after partitioning
        pivot = partition(array, low, high)

        # Recursively sort elements before and after partition
        quick_sort(array, low, pivot - 1)  # Sort the left half
        quick_sort(array, pivot + 1, high)  # Sort the right half

def partition(array, low, high):
    # Choose the pivot (first element)
    pivot = array[low]
    i = low + 1  # Start just after the pivot
    j = high

    while True:
        # Move `i` to the right as long as array[i] <= pivot
        while i <= j and array[i] <= pivot:
            i += 1
        
        # Move `j` to the left as long as array[j] >= pivot
        while i <= j and array[j] >= pivot:
            j -= 1

        # If the pointers crossed, break
        if i <= j:
            # Swap array[i] and array[j]
            array[i], array[j] = array[j], array[i]
        else:
            break

    # Swap the pivot element with array[j] (put pivot in its correct place)
    array[low], array[j] = array[j], array[low]

    # Return the pivot index
    return j

# Example usage
array = [5, 8, 1, 2, 6, 3, 9]
quick_sort(array, 0, len(array) - 1)
print("Sorted array:", array)
