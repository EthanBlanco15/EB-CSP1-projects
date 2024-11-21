#Ethan Blanco, ProficiencyTest: Rock, Paper, Scissors
import random
while True:
    pChoice = 1
    cChoice = 2
    action = input("""What would you like to do?

        Enter 1 to leave

        Type anything to play/continue:\n""")
    if action =="1":
        print("Bye bye!")
        break
    new_action = input("""Let's play! Rock, paper or scissors?
                           
        Enter 1 to play ROCK              
        
        Enter 2 to play PAPER                   
                            
        Enter 3 to play SCISSORS\n""")
    
    cChoice = str(random.randint(1, 3))
    print("Computer choice is", cChoice)
    if new_action =="1" and cChoice =="1":
        print("Tie!")
    elif new_action =="1" and cChoice =="2":
        print("Computer wins!")
    elif new_action =="1" and cChoice =="3":
        print("You win!")
    elif new_action =="2" and cChoice =="1":
        print("You win!")
    elif new_action =="2" and cChoice =="2":
        print("Tie!")
    elif new_action =="2" and cChoice =="3":
        print("You lose!")
    elif new_action =="3" and cChoice =="1":
        print("You lose!")
    elif new_action =="3" and cChoice =="2":
        print("You win!")
    elif new_action =="3" and cChoice =="3":
        print("Tie!")
    else:
        print("This doesn't work... Maybe try something else")
        break