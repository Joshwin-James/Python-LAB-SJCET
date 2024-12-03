Total_sticks=16
player1=input("Enter the Name Of Player1 :")
player2=input("Entetr the name of Player2 :")
current=0
while Total_sticks>1:

    while True:
        current=player1
        print(player1, "pick 1,2 or 3 Sticks :", end='')
        p1=int(input())
        if p1>0 and p1<4:
            Total_sticks-=p1
            print("Remaining no of sticks =",Total_sticks)
            break
        else:
            print("Invalid input you can only take values up to 3")
            continue

    while True :
        current=player2
        print(player2,"pick 1,2 or 3 Sticks :",end='')
        p2=int(input())
        if p2>0 and p2<4:
            Total_sticks-=p2
            print("Remaining no of sticks =", Total_sticks)
            break
        else:
            print("Invalid input")
            print()
            continue
    if Total_sticks<=0:
        print(current,"IS THE LOSER")
        break