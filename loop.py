row=int(input("Ente the number of rows required :"))
for i in range(row):
    for j in range(i+1):
        print("*",end=' ')
    print()

print()
print()
for i in range(row-1,-1,-1):
    for j in range(i+1):
        print("*",end=' ')
    print()
print()

for i in range(row+1):
    for j in range(row-i):
        print(' ',end=' ')
    for k in range((2*i)-1):
        print("*",end=' ')
    print()
print()
for i in range(row,-1,-1):
    for j in range(row-i):
        print(' ',end=' ')
    for k in range((2*i)-1):
        print("*",end=' ')
    print()