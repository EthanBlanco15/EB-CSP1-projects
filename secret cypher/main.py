#Ethan Blanco, ProficiencyTest: Secret Cypher

code =input("What would you like your code to be? Please input an available word.\n ")
cypher = "" # Empty string
def converter(code, cypher):
    for letter in code: # Normally, ord and chr functions only take one identation, but with the for loop, it takes it letter by letter.
        letter = ord(letter) # Ord turns strings into integers, thats the conversion here.
        letter += 1 # We're adding one extra here to make it more mixed.
        letter = chr(letter) # using the chr function here converts the integers back into a string.
        cypher += letter #Adding the empty string and function of chr and ord.
    print(cypher) # We left the print function here, but made the identation less to not include everything.

converter(code, cypher) 