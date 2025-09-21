
#TASK 1
list1 = []
list2 = []

count = int(input("How many numbers do you want to add in list? 3 or 5  "))
for i in range(count):
    element = int(input(f"Enter element {i+1}: "))
    list1.append(element)

count1 = int(input("How many numbers do you want to add in list? 3 or 5  "))
for i in range(count1):
    element1 = int(input(f"Enter element {i+1}: "))
    list2.append(element1)

merged_list = list1 + list2

print("\nUnsorted outpt: ", merged_list)
merged_list.sort()
print("Sorted output: ",  merged_list)



#TASK 2
#my list is already sorted 
print("\nSmallest Number is: ", merged_list[0])    
print("Largest Number is: ", merged_list[-1])     

#a=0
#for a in merged_list:
#    if merged_list[a] > merged_list[a+1]:
#        print("Smallest Number is: ", merged_list[a+1])


#TASK 3
birthdays = {
    "Basit Ali": "03/14/2004",
    "Hasan Ali": "01/17/2000", 
    "Masood Abbas": "12/10/2003"
}

print("\n Welcome to the birthday dictionary. We know the birthdays of: ")
print("1. Basit Ali", "2. Hasan Ali", "3. Masood Abbas")
c = int(input("Enter your choice: "))

if c == 1:
    print("Birthday of Basit is: ", birthdays["Basit Ali"])
elif c == 2:
    print("Birthday of Hasan is: ", birthdays["Hasan Ali"])
elif c == 3:
    print("Birthday of Masood is: ", birthdays["Masood Abbas"])


#TASK 4
employee = {
    "Name": "Talha Mehmood",
    "Age": "20",
    "Salary": "180,000",
    "City": "Attock"
}

print("\n Welcome to the Employee details dictionary.")
print("1. Name", "2. Age", "3. Salary", "4. City")
c = int(input("Enter your choice: "))

if c == 1:
    print(employee["Name"])
elif c == 2:
    print(employee["Age"])
elif c == 3:
    print(employee["Salary"])
elif c== 4:
    print(employee["City"])
