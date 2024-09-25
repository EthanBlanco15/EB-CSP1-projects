#Ethan Blanco, Skill Practice: Average Grade

math = input("Enter your Math grade;")
math = float(math)
english = input("Enter your English grade;")
english = float(english)
art = input("Enter your Art grade;")
art = float(math)
cs = input("Enter your Computer Science grade;")
cs = float(cs)
leadership = input("Enter your Leadership grade;")
leadership = float(leadership)
health = input("Enter your Health grade;")
health = float(health)
avg_grade = (math + english + art + cs + leadership + health)/6
print("Your average grade is", avg_grade)