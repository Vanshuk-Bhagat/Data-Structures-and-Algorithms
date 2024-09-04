print("How many element to store inside the array", end="")
num = input()
arr = []
print("\n Enter", num, "Element:", end="")
num = int(num)
for i in range(num):
    element = input()
    arr.append(element)

print("\n The array elements are: ", end="")
for i in range(num):
    print(arr[i], end=" ")
