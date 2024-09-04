num=int(input("Enter the max number"))

odd_num = []
for i in range(1, num):
    if i % 2 == 1:
        odd_num.append(i)
print(odd_num)
