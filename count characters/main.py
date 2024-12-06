#Ethan Blanco, SkillPractice: Counting characters
grid = [

['A', 'B', 'C', 'A', 'D'],

['C', 'A', 'B', 'D', 'E'],

['A', 'D', 'C', 'E', 'A'],

['B', 'A', 'C', 'A', 'D'],

['D', 'C', 'B', 'E', 'A'] ]
a = 0
b = 0
c = 0
d = 0
e = 0
for row in grid: #This for loop is grabbing a random new variable the computer not knows, and puts it into the list variable 'grid' it does know.
    for spot in row: #Now this other for loop which with the one above together is a nested loop, takes a random variable and takes the other recent variable into the already present grid.
        if spot == 'A': #For loops already go over everything that is a part of it, so it'll go over this grid list and everything part of it. This is now checking for anything saying "A" and do the following.
            a += 1
        if spot == "B":
            b += 1
        if spot == "C":
            c += 1
        if spot == "D":
            d += 1
        if spot == "E":
            e += 1
    print(f"There are {a} amount of A's, {b} amount of B's, {c} amount of C's, {d} amount of D's and {e} amount of E's \n")