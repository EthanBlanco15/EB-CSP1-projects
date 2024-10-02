#Ethan Blanco, SkillPractice: Palindrome

pal = input("Enter your Palindrome word!;")

if pal == pal[::-1]:
    print(pal)
else:
    print("This isn't a Palindrome bro!")