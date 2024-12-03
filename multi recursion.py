'''Author: Joshwin James
Date:3-12-24
Multipilication of 2 numbers using recursion'''
def multi(n1,n2):
    if n2==1:
        return n1
    else:
        return n1+multi(n1,n2-1)
print(multi(4,5))