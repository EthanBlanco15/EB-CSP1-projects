#Ethan Blanco, RAID: Character Creator

health = 0
strength = 0
dexterity = 0
intelligence = 0
name = input("What is your player name?\n ")
race = input("What would you like your race to be?\n ")
class_ = input("Which class would you like to use?\n Wizard\n Paladin\n Gladiator\n Assassin\n ")
if class_ =="Wizard":
    health =+ 150
    strength =+ 25
    dexterity =+ 50
    intelligence =+ 75

elif class_ =="wizard":
    health =+ 150
    strength =+ 25
    dexterity =+ 50
    intelligence =+ 75

elif class_ =="Paladin":
    health =+ 125
    strength =+ 60
    dexterity =+ 45
    intelligence =+ 50

elif class_ =="paladin":
    health =+ 125
    strength =+ 60
    dexterity =+ 45
    intelligence =+ 50

elif class_ =="Gladiator":
    health =+ 200
    strength =+ 100
    dexterity =+ 25
    intelligence =+ 10

elif class_ =="gladiator":
    health =+ 200
    strength =+ 100
    dexterity =+ 25
    intelligence =+ 10

elif class_ =="Assassin":
    health =+ 100
    strength =+ 75
    dexterity =+ 100
    intelligence =+ 60

elif class_ =="assassin":
    health =+ 100
    strength =+ 75
    dexterity =+ 100
    intelligence =+ 60

else:
    print("Invalid, sorry!")
    
stats = [health, strength, dexterity, intelligence]
print("Here are your stats", name, "your race is", race, "and your stats are listed in health, strength, dexterity and intelligence!\n ", stats)