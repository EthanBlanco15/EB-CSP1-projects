#Ethan Blanco, ProficiencyTest: Shopping List Manager
list = [] #Makes the variable list for what they need to add.
def add(): #Defining the add() below
    object = input("What item do you want to add?") #Works as a variable, object and is asking the user a question.
    list.append(object) #Adds a variable or in this case an item to the list.
    print(list) #Obviously, prints out the list to show progress.

def remove(): #Defining the remove() below for use.
    object = input("What item do you want to remove?") #Works as a variable like before.
    list.remove(object) #Rather than adding, you remove a variable from the list, an object.
    print(list)
while True:

    action = input("""What would you like to do?

                                  Enter 1 to add item

                                  Enter 2 to remove item

                                  Enter 3 to leave the list:\n""")

    if action =="1":

        add()

    elif action =="2":

        remove()

    else:

        print("Have a nice day!")

        break