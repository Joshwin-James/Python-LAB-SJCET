'''Author: Joshwin James
Date:3-12-24
factorial using recursion'''
def factorial(n):
    if n==1:
        return 1
    else:
        return n*factorial(n-1)
print(factorial(7))
