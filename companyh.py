employee=[
    ("john","manager",90000.00),
    ("jose","finance",47000.00),
    ("kurian","marketing",20000.00)

]
annual_expense=0
for i in employee:
    name,department,salary=i
    print("Employee name=",name,"Department=",department,"salary",salary)
    annual_expense+=salary*12
print("annual expense :",annual_expense)
range=int(input("Enter the salary range"))
for i in employee:
    name,department,salary=i
    if salary>range:
        print(name)
