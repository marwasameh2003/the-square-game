# this is square game
# done by : MARWA SAMEH , student in FCAI
# 4/3/2022
#supervised by DR.MOHAMMED EL RAMMLY
# let us create the 2D list that will appear to the players
listhorizontal = [' 1  2  3  4']
listspaces = [' ________']
boardgame = [[' 1',' 2',' 3',' 4'],[' 5',' 6',' 7',' 8'],[' 9','10','11','12'],['13','14','15','16']]
listvertical = ['1','2','3','4','1','2','3','4','1','2','3','4','1','2','3','4','1','2','3','4','1','2','3','4','1','2','3','4','1','2','3','4','1','2','3','4','1','2','3','4','1','2','3','4','1','2','3','4','1','2','3','4','1','2','3','4','1','2','3','4','1','2','3','4','1','2','3','4','1','2','3','4','1','2','3','4''1','2','3','4','1','2','3','4','1','2','3','4']
listspace2 = ['|','|','|','|','|','|','|','|','|','|','|','|','|','|','|','|','|','|','|','|','|','|','|','|','|','|','|','|','|','|','|','|','|','|','|','|','|','|','|','|','|','|','|','|','|','|','|','|','|','|','|','|','|','|','|','|','|','|','|','|','|','|','|','|','|','|','|','|','|','|','|','|','|','|','|','|','|','|','|','|','|','|','|','|','|','|','|','|','|','|']
x = 0
y = 0
#here is the function containing the displayed board
def displayedboard():
    for n in listhorizontal:
        print(n)
    for h in listspaces:
        print(h)
    for element in boardgame:

        global x
        global y

        for i in element:
                print(i, end=" ")

        print(" ",listspace2[y],listvertical[x])
        x+=1
        y+=1





counter = 0
# here is the function that declares the winner depending on the counter
def winner():
    if counter%2!=0:
        print("player 1 is the winner , congratulations")
    else:
        print("player 2 is the winner , congratulations")
endgame = True
# this is the condition that will either let the game completes or ends and declares the winner
#if there are two boxes in the table beside each other or under each other this means that the game completes, else the game ends
def endgamecondition():
    while boardgame[0][0]=="1" and boardgame[0][1]=="2" or boardgame[0][0]=="1" and boardgame[1][0]=="5" or boardgame[0][1]=="2" and boardgame[0][2]=="3" or boardgame[0][1]=="2" and boardgame[1][1]=="6" or boardgame[0][2]=="3" and boardgame[0][3]=="4" or boardgame[0][2]=="3" and boardgame[1][2]=="7"  or boardgame[0][3]=="4" and boardgame[1][3]=="8" or boardgame[1][0]=="5"and boardgame[1][1]=="6" or boardgame[1][0] =="5" and boardgame[2][1]=="10"  or boardgame[1][1]== "5" and boardgame[1][2]=="6"  or boardgame[1][1]=="5" and  boardgame[2][1]=="9"  or boardgame[1][2]=="7" and boardgame[1][3]=="8"  or boardgame[1][2] =="7"and  boardgame[2][2]=="11"  or boardgame[1][3]=="8" and boardgame[2][3]=="12"  or boardgame[2][0] =="9" and boardgame[2][1]=="10"  or boardgame[2][0]=="9" and boardgame[3][0]=="13"  or boardgame[2][1]=="10" and boardgame[2][2]=="11"  or boardgame[2][1] =="10" and  boardgame[3][1]=="13"  or boardgame[2][2] =="11" and  boardgame[2][3]=="12"  or boardgame[2][2] =="11" and boardgame[3][2]=="15"  or boardgame[2][3]=="12" and boardgame[3][3]=="16"  or boardgame[3][0]=="13"and boardgame[3][1]=="14"  or boardgame[3][1]=="14" and boardgame[3][2]=="15"  or boardgame[3][2] =="15" and  boardgame[3][3]=="16" :
        endgame = False
        player_play()
        if endgame is True:
            winner()
#this function lets the player to choose 2 numbers with respect to:
# the number chosen was not chosen before
# the two numbers must form a rectangle by making the absolute difference between them either 1 or 4
# the number is a valid one not a negative one or a letter
# the counter is to show which one is the winner since the same function will work for both players
#so if the counter is odd, this means player one is playing. and if the counter is even this means player two is playing
# each time the player plays the game shows him the boardgame
def player_play():
    global counter
    counter+=1
    displayedboard()
    row1, column1 = map(int, input("row,column:").split())
    if  boardgame[row1 - 1][column1 - 1] == " x":
        print("invalid input ")
        row1, column1 = map(int, input("row,column:").split())
        boardgame[row1 - 1][column1 - 1] = " x"
    else:
        boardgame[row1 - 1][column1 - 1] = " x"
        displayedboard()
        row2, column2 = map(int, input("row,column:").split())
        if  boardgame[row2 - 1][column2 - 1] == " x":
            print("invalid input ")
            row2, column2 = map(int, input("row,column:").split())
            boardgame[row2 - 1][column2 - 1] = " x"
        else:
            boardgame[row2 - 1][column2 - 1] = " x"
            if abs(int(row2)-int(row1))!= 1 or abs(int(column2)-int(column2))!= 4:
                print("invalid input please enter values that create rectangle: ")
                row1, column1 = map(int, input("row,column:").split())
                if boardgame[row1 - 1][column1 - 1] == " x":
                    print("invalid input ")
                    row1, column1 = map(int, input("row,column:").split())
                    boardgame[row1 - 1][column1 - 1] = " x"
                else:
                    boardgame[row1 - 1][column1 - 1] = " x"
                    displayedboard()
                    row2, column2 = map(int, input("row,column:").split())
                    if boardgame[row2 - 1][column2 - 1] == " x":
                        print("invalid input ")
                        row2, column2 = map(int, input("row,column:").split())
                        boardgame[row2 - 1][column2 - 1] = " x"
                    else:
                        boardgame[row2 - 1][column2 - 1] = " x"



# here all the functions are collected in only one function and in order so it can be easily called.
def game():
    player_play()
    endgamecondition()
    winner()
    displayedboard()





game()