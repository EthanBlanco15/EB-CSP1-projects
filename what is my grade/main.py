#Ethan Blanco, SkillPractice: What is My Grade

#Grading Scale: Mark/Min Percent; A/ 94 | A-/ 90 | B+/ 87 | B/ 84 | B-/ 80 | C+/ 77 | C/ 74 | C-/ 70 | D+/ 67 | D/ 64 | D-/ 60 | F/ 0
grade = (input("What is your grade percentage for any current classes?:\n"))
if grade =="":
    print("You wrote nothing! Try again please.\n ")
elif float(grade) >= 110.00:
    print("This is... A bit too high, are you sure this is your grade?\n")
elif float(grade) >= 100.00:
    print("Whoah! You definitely have an A! Great work!\n")
elif float(grade) >= 94.00:
    print("Your grade has a straight A! Congrats!\n")
elif float(grade) >= 90.00:
    print("Your grade has an A-. Nice!\n")
elif float(grade) >= 87.00:
    print("Your grade is a B+. Almost there to an A!\n")
elif float(grade) >= 84.00:
    print("Your grade is a straight B. Fantastic! Lets work harder!\n")
elif float(grade) >= 80.00:
    print("Your grade has a B-. Careful not to fall behind!\n")
elif float(grade) >= 77.00:
    print("Your grade is a C+. Hang in there!\n")
elif float(grade) >= 74.00:
    print("Your grade has a straight C. You got this!\n")
elif float(grade) >= 70.00:
    print("Your grade has a C-. Don't give up just yet!\n")
elif float(grade) >= 67.00:
    print("Your grade is a D+. You're falling behind! Seek help to get your grade up before it's too late!\n")
elif float(grade) >= 64.00:
    print("Your grade has a straight D. Come on, I believe in you, you got this!\n")
elif float(grade) >= 60.00:
    print("Your grade has a D-... There's sill a chance!\n")
elif float(grade) < 0:
    print("I don't think this is even possible, you should type in something else.")
elif float(grade) < 59.99:
    print("An F... Maybe it's just for now?")
else:
    print("This isn't an available value! Please type in a number instead.")