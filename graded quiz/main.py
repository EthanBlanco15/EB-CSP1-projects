#Ethan Blanco, ProficiencyTest: Graded Quiz.

mars = input("Do we live on Mars? ")
heart = input("Do we have a heart? ")
english = input("Do we speak English? ")
question = input("Is this a question? ")
seven = input("Is seven a lucky number? ")

score = 0

if mars == "no" : 
    score += 1
if heart == "yes" : 
    score += 1
if english == "yes" : 
    score += 1
if question == "yes" : 
    score += 1
if seven == "yes" : 
    score += 1

print(score)