def right_tri(list):
    if list[2]**2 + list[1]**2==list[0]**2:
        print('\n'''"The Triangle Given is a Right angled triangle")
    else:
        print('\n'"NO!")

list=[]
for i in range(3):
    s=int(input("Enter the side :"))
    list.append(s)
    list.sort(reverse=True)

right_tri(list)