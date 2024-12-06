#Ethan Blanco, ProficiencyTest: Simple Quiz Game
while True:
    game = input("""1. How many sides does a triangle have?
             a. 1 Side
             b. 3 Sides
             c. 8 Sides
             d. No Sides
             Press space to quit\n""")
    if game =="b":
        hGame = input("""Good! Here's a HARDER question!
                        2. How many sides does a trapezoid have?
                    a. 2 Sides
                    b. 4 Sides
                    c. 8 Sides
                    d. 14 Sides\n""")
        if hGame == "a" and "c" and "d":
            print("Darn! Let's take a step back and try an easier question than this one.")
            continue
        elif hGame == "b":
            haGame = input("""Fantastic! How about a harder question?
                        3. How many sides does an octagon have?
                    a. 8 sides
                    b. 4 sides
                    c. 10 sides
                    d. 14 sides\n""")
            if haGame =="b" and "c" and "d":
                print("Wrong one, let's start again.")
                continue
            elif haGame =="a":
                harGame = input("""Great! Let's move onto the last and hardest question yet!
                        4. What shape has the most sides?        
                    a. Octagon
                    b. Trapezoid
                    c. Dodecagon
                    d. Decagon\n""")
                if harGame =="a" and "b" and "d":
                    print("Oops! Wrong answer, let's start again.")
                    continue
                elif harGame =="c":
                    print("Fantastic! You got all the question right!")
                    break

    elif game =="a" and "c" and "d":
        eGame = input("""Wrong choice, here's an easier question for you!
                        -1. How many sides does a circle have?
                  a. 4 Sides
                  b. 10 Sides
                  c. 1 Sides
                  d. No sides
          \n""")
        if eGame =="d":
            print("Nice! Let's go back to the original question.")
            continue
        elif eGame =="a" and "b" and "c":
            eaGame = input("""Not quite... Let's try something a bit easier!
                        -2. What most likely represents a triangle?
                    a. A pyramid
                    b. A box
                    c. A board
                    d. A ball\n""")
            if eaGame == "a":
                print("Nice! Let's go back to the original question.")
                continue
            elif eaGame == "b" and "c" and "d":
                easGame = input("""Almost there, try another easier question!
                        -3. What most likely represents a circle?
                    a. A ball           
                    b. A tower           
                    c. A box
                    d. An oval\n""")
                if easGame == "a":
                    print("Nice! Let's go back to the original question.")
                    continue
                if easGame == "b" and "c" and "d":
                    easyGame = input("""Last question now, try your best on this one or the game ends!
                        -4. What does a box look like?
                    a. A triangle
                    b. A triangle
                    c. A square
                    d. A circle\n""")
                if easyGame == "c":
                    print("Nice! Let's go back to the original question.")
                    continue
                elif easyGame == "b" and "c" and "d":
                    print("I have no more questions to give, better luck next time!")
                    break
    elif game ==" ":
        print("Okay, goodbye!")
        break
    else:
        print("This doesn't work, try again.")
        continue