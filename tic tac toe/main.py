#Ethan Blanco, ProficiencyTest: Tic Tac Toe
import random

def Check():
    global Tie
    global End
    # Tie
    Tie = True
    End = True
    for row in grid1:
        for space in row:
            if space != "x" or space != "o":
                Tie = False
                End = False
    if Tie == True:
        print("Draw")
    # X row
    for row in grid1:
        if row ==[ticTacToeGame, ticTacToeGame, ticTacToeGame]:
            End = True
            print("Player wins!") 
    # O row
    for row in grid1:
        if row ==[comp_, comp_, comp_]:
            End = True
            print("Computer wins!") 

    # Diagonal
    if grid1[0][0] ==ticTacToeGame and grid1[1][1]==ticTacToeGame and grid1[2][2]==ticTacToeGame:
        End = True
        print("Player wins!")
    if grid1[0][0] ==comp_ and grid1[1][1]==comp_ and grid1[2][2]==comp_:
        End = True
        print("Computer wins!")

    # Player column
    xColumn = 0
    for row in grid1:
        if row[0] ==ticTacToeGame:
            xColumn += 1
    if xColumn ==3:
        End = True
        print("Player wins!")        
    xColumn = 0

    for row in grid1:
        if row[1] ==ticTacToeGame:
            xColumn += 1
    if xColumn ==3:
        End = True
        print("Player wins!")        
    xColumn = 0

    for row in grid1:
        if row[2] ==ticTacToeGame:
            xColumn += 1
    if xColumn ==3:
        End = True
        print("Player wins!")
    xColumn = 0

    # Comp column
    oColumn = 0
    for row in grid1:
        if row[0] ==comp_:
            oColumn += 1
    if oColumn ==3:
        End = True
        print("Computer wins!")       
    oColumn = 0

    for row in grid1:
        if row[1] ==comp_:
            oColumn += 1
    if oColumn ==3:
        End = True
        print("Computer wins!")         
    oColumn = 0

    for row in grid1:
        if row[2] ==comp_:
            oColumn += 1
    if oColumn ==3:
        End = True
        print("Computer wins!")
    oColumn = 0
while True:
    grid1 = [ 
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9] ]
    try:
        game = int(input("""Would you like to play?
                
             Enter 1 to play
             
             Enter 2 to quit
             \n"""))
    except:
        print("This doesn't work")
        continue
    if game ==1:
        print("""Lets play!
          
          here's the grid
                \n""")
        for row in grid1:
            print(row)
    elif game ==2:
        print("Okay, goodbye!")
        break
    End = False
    grid1 = [ 
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9] ]
    try:
        ticTacToeGame = input("""
            Press x to be 'X'
            
            Press o to be 'O'
                                
            Enter nothing to quit:\n""")
    except:
            print("This doesn't work, maybe try another thing?")
            continue
    if ticTacToeGame =="":
        print("Okay, goodbye!")
        break
    elif ticTacToeGame =="x" or ticTacToeGame =="o":
        if ticTacToeGame =="x":
            comp_ = "o"
        elif ticTacToeGame =="o":
            comp_ = "x"
            
        while True:
            try:
                pChoice = int(input("""Let's start!
                        Where would you like to place your spot in the grid?
                \n"""))
            except:
                print("This doesn't work")
                continue
            for row in grid1:
                print(row)
            Check()
            if End == True:
                break
            for rowIndex, row in enumerate(grid1):
                for spotIndex, spot in enumerate(row):
                    if spot == pChoice: # Capital O's numerical value is 79, and X is 88
                        grid1[rowIndex][spotIndex] = ticTacToeGame
            print("")
            for row in grid1:
                print(row)
            Check()
            if End == True:
                break
            cChoiceWorked = False
            while cChoiceWorked == False:
                cChoice = int(random.randint(1, 9))
                for rowIndex, row in enumerate(grid1):
                    for spotIndex, spot in enumerate(row):
                        if spot == cChoice:
                            grid1[rowIndex][spotIndex] = comp_
                            cChoiceWorked = True