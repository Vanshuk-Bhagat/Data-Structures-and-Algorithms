# Function to perform binary search on a sorted array
def binary_search(array, target):
    # Initialize the low and high pointers
    low = 0
    high = len(array) - 1

    # Loop until the search space is exhausted
    while low <= high:
        # Calculate the middle index
        mid = (low + high) // 2

        # Check if the middle element is the target
        if array[mid] == target:
            return mid  # If found, return the index of the target

        # If the target is smaller than the middle element, search the left half
        elif array[mid] > target:
            high = mid - 1

        # If the target is larger than the middle element, search the right half
        else:
            low = mid + 1

    # If the target is not found, return -1
    return -1

# Example array (unsorted)
array = [1, 4, 5, 3, 2, 6, 7, 8, 12]

# Sort the array before performing binary search (binary search requires a sorted array)
array.sort()
print(array)  # Print the sorted array to the user

# Prompt the user to input the number they want to find
target = int(input("Enter the number that you want to find: "))

# Perform binary search and store the result (index or -1)
result = binary_search(array, target)

# Check if the target was found
if result != -1:
    # If found, print the index at which the target is located
    print(f"The number {target} is found at index {result}.")
else:
    # If not found, print a message indicating the target is not in the array
    print(f"The number {target} is not found in the array.")
