tmp=int(input("Enter temperature:"))
typ=input("Is this in Fahrenheit or celcius")
if typ in "Cc":
    f=(9/5*tmp)+32
    print(tmp,"degree celcuis is ",f,"degree faranheit")
elif typ in "fF":
    c=5/9*(tmp-32)
    print(tmp,"degree faranheit is ",c,"degree celcius")

