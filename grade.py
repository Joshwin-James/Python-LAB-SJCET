'''
Author :Joshwin James
Date :1-10-2024
To find grade of a student
'''
name=input("Enter the name of the Student :")
roll=int(input("Enter the roll no of student :"))
print()
phy=int(input("Enter the mark of Physics :"))
mat=int(input("Enter the mark of Maths :"))
che=int(input("Enter the marks of Chemistry :"))
eng=int(input("Enter the marks of English :"))
com=int(input("Enter the marks of Computer :"))
print()
print("Calculating Grades")
print("Name of student :",name)
print("Roll no of student :",roll)
total=phy+mat+che+eng+com
print("Total marks of Student :",total)
grade=(total/500)*100
if grade>=97:
    print("Grade of student is A+")
elif grade>=90:
    print("grade of student is A")
elif grade>=80:
    print("grade of student is B")
elif grade>=70:
    print("grade of student is C")
elif grade>=60:
    print("grade of student is D")
elif grade>=50:
    print("grade of student is E")
elif grade<50:
    print("grade of student is F"
          " student is FAILED!!!")


