#Ethan Blanco, ProficiencyTest: Shopping List Manager

cart = input("Would you like to 'add' an item to your shopping cart, 'remove' or quit the program?")
add = print("What would you like to add to your cart?")
while True:
    action = input("""What would you like to do?
                   Enter 'add' to add item
                   Enter 'remove' to remove item
                   Etner 'quit' to leave the list:\n""")
if action =="add":
    add()
elif action =="remove":
    remove()
else:
    print("Have a great day!")
    #break
