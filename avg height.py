'''Author : Joshwin James
Date : 15-10-2024
To check the average heighty of boys and girls '''
n=int(input("Enter the number of students"))
btotal=0
bh=0
gtotal=0
gh=0
for i in range(1,n+1):
    g=input("Enter the gender as M or F")
    h=int(input("enter the height in cm"))
    if g in "Mm":
        btotal+=1
        bh+=h
    elif g in "fF":
        gtotal+=1
        gh+=h
bavg=bh/btotal
print("Average height of boys =",bavg)
gavg=gh/gtotal
print("Average height of girls =",gavg)
