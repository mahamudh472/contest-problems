for i in range(int(input())):
    num = int(input())
    player1_inp = input().split()
    player2_inp = input().split()
    player3_inp = input().split()
    player1 = 0
    player2 = 0
    player3 = 0
    for i in player1_inp:
        if i not in player2_inp and i not in player3_inp :
            player1 +=3
        elif i not in player2_inp or i not in player3_inp :
            player1 +=1
        else:
            player1 +=0
    for i in player2_inp:
        if i not in player1_inp and i not in player3_inp :
            player2 +=3
        elif i not in player1_inp or i not in player3_inp :
            player2 +=1
        else:
            player2 +=0
    for i in player3_inp:
        if i not in player2_inp and i not in player1_inp :
            player3 +=3
        elif i not in player2_inp or i not in player1_inp :
            player3 +=1
        else:
            player3 +=0
    print(player1, player2, player3)