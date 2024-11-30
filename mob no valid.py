def valid_no():
    no=input("Enter The Mobile No :")
    if len(no)==10 and no[0] in '789' :
        print('Valid')
    else:
        print("Not valid")
valid_no()

