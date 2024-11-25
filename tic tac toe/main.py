#Ethan Blanco, ProficiencyTest: Tic Tac Toe
grid1 = ["1, 2, 3"]
grid2 = ["4, 5, 6"]
grid3 = ["7, 8, 9"]
import random
while True:
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
          
          here's the grid\n
          """, grid1, grid2, grid3)
    if game ==2:
        print("Okay, goodbye!")
        break