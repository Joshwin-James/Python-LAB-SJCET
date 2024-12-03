'''Author: Joshwin James
Date:3-12-24
Addition of 2 numbers using recursion'''
def addition(n1,n2):
    if n2==0:
        return(n1)
    else:
        return addition(n1+1,n2-1)
a=addition(1000,300)
print(a)