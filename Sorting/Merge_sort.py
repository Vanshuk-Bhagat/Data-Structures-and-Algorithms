def merge_sort(array):
    # Base case: if the array has 1 or fewer elements, it's already sorted
    if len(array) <= 1:
        return array

    # Split the array into two halves
    mid = len(array) // 2
    l_half = array[:mid]
    r_half = array[mid:]

    # Recursively sort each half
    l_half = merge_sort(l_half)
    r_half = merge_sort(r_half)

    # Merge the sorted halves
    return merge(l_half, r_half)

def merge(left, right):
    new = []
    i, j = 0, 0

    # Merge the two sorted halves into a new list
    while i < len(left) and j < len(right):
        if left[i] < right[j]:
            new.append(left[i])
            i += 1
        else:
            new.append(right[j])
            j += 1

    # Append any remaining elements from the left and right halves
    new.extend(left[i:])
    new.extend(right[j:])
    return new

# Example usage
array = [89, 23, 45, 67, 22, 44, 69]
sorted_array = merge_sort(array)
print("Sorted array:", sorted_array)
