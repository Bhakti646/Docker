empname = []
emp = input("Enter 5 Employee names separated by , :")
empname = emp.split(",")
print(empname)
search = input("enter name you wawnt to found:")
for i in empname:
    if (search == i):
        flag = 1
        break
    else:
        flag = 0
if (flag ==1):
    print("Employee is part of organization")
else:
    print("Employee data base not available")
            

