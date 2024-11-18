#Ethan Blanco, ProficiencyTest: Authorized

users = ["abc404", "zenith", "Bob", "nagi", "Leo", "gen", "Shin", "appleplayer"]
auth = input("Enter your username:\n ")
if auth == "":
    print("No input seen.")
elif auth == "abc404":
    print("Hello abc404, welcome back.\n ")
elif auth == "zenith":
    print("Hello zenith, welcome back.\n ")
elif auth == "Bob":
    print("Sorry Bob, you do not have an authorized account, would you like to register?\n ")
elif auth == "nagi":
    print("Welcome back Admin user nagi.\n ")
elif auth == "Leo":
    print("Hello Leo, welcome back.\n ")
elif auth == "gen":
    print("Hello gen, welcome back.\n ")
elif auth == "Shin":
    print("Welcome back Admin user Shin.\n ")
elif auth == "appleplayer":
    print("Sorry apple player, you do not have an authorized account, would you like to register?\n ")
else: 
    print("This isn't available right now, use another input.")