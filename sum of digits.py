'''Author : Joshwin James
Date : 15-10-2024
To find sum of digits of a number'''
no=int(input("Enter a number"))
sum = 0
while no>0:
    temp=no%10
    sum+=temp
    no=no//10
print(sum)
