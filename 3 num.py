'''Author : Joshwin James
Date : 15-10-2024
To Find largest among 3 numbers'''
no1=(int(input("Enter The first number :")))
no2=(int(input("Enter The second number :")))
no3=(int(input("Enter The third number :")))
tmp=0
if no1>no2:
    tmp=no1
else:
    tmp=no2
if no3>tmp:
    print("Largest is ",no3)
else:
    print("Largest is ", tmp)