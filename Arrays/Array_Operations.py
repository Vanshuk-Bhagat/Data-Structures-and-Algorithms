#Creating an array with expenses
#Assume 2220 = Jan , 2350 = feb, 2600 = march, 2130 = april
exp=[2220,2350,2600,2130]

# In Feb, how many dollars you spent extra compare to January?

print("Amount of Salary spend in feb =",exp[1]-exp[0])
# Find out your total expense in first quarter (first three months) of the year.

print("Total expenses in 1st quater is =",exp[0]+exp[1]+exp[2])
# Find out if you spent exactly 2000 dollars in any month
for i in exp:
    if i==2000:
        print(i)
else:
  print("No expenses= 2000")
#  June month just finished and your expense is 1980 dollar. Add this item to our monthly expense list
exp1=exp
exp1.append(1980)
print(exp1)
#You returned an item that you bought in a month of April and
#got a refund of 200$. Make a correction to your monthly expense list
#based on this

exp[3] = exp[3] - 200
print(exp) 