array = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
a = int(input("Enter the number: "))

# Initialize a flag to indicate if the number is found
found = False

for i in range(len(array)):
    if array[i] == a:
        print(f"{a} number is found at index {i}")
        found = True
        break  # Exit the loop once the number is found

if not found:
    print(f"{a} number not found")


