#Ethan Blanco, ProficiencyTest: Multiplication Table

num = int(input("From 0-12, which number would you like to see the multiples of?\n "))
for factor in range(13): #The factor here times everything from 1-12
    print(num * factor) #This is multiplying the input by numbers the factor represents which is 1-12