inventory=[
    ("dairymilk",15,30),
    ('kitkat',20,40),
    ('milkybar',30,10)
]
list=[]
for i in inventory:
    name,quantity,unitprice=i
    totalvalue=quantity*unitprice
    print("Item_name :",name,"Total_value :",totalvalue)
    list.append(totalvalue)

    print()
print('Max value: ',max(list))