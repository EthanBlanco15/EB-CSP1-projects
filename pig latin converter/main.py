#Ethan Blanco, SkillPractice: Pig Latin Converter

word = input("Which word would you like to be converted into pig latin?")

def conver(word): #We define the converter with our last variable for the users input.
    ay = word[0] + "ay" #We take a new variable, equal it to our last and add 1 but put 0 because of python syntax rules, then as well adding the actual word "ay"
    print(word[1:]+ay) #From here, we print our word, removing the first part of the string user had put, adding the ay variable.

conver(word) #This is ending the function and making it somewhat work.