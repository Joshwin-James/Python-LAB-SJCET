list=[]
while True:
    inp=int(input("Enter the Number :"))
    list.append(inp)
    ch=input("Want to add more?, y/n :")
    if ch=='n':
        break
print(list)
print("To input second list ")
list2=[]
while True:
    inp=int(input("Enter the Element :"))
    list2.append(inp)
    ch=input("Want to add more?, y/n :")
    if ch=='n':
        break
print(list2)

list3=list+list2
even=[]
odd=[]
mainlist=[]
for i in list3:
    if i%2==0:
        even.append(i)
    else:
        odd.append(i)
even.sort()
odd.sort()
mainlist=even+odd
print()
print("THE SORTED LIST IS:")
print(mainlist)