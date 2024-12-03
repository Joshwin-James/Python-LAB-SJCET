'''Author: Joshwin James
Date:3-12-24
GCD of 2 numbers using recursion'''
def gcd(n1,n2):
    if n1%n2==0:
        return n2
    else:
        return gcd(n2,n1%n2)
print(gcd(1220,512))
