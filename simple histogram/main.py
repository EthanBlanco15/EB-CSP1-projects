#Ethan Blanco, RAID: Simple Histogram

listnum = int(input("Your first number.\n "))
listnum2 = int(input("Your second number.\n "))
listnum3 = int(input("Your third number.\n "))
listnum4 = int(input("Your fourth number.\n "))
listnum5 = int(input("Your fifth number.\n "))

numlist = [listnum, listnum2, listnum3, listnum4, listnum5]
for number in numlist:
    i = ""
    for item in range(number):
        i += "*"
    print(f"{number}: {i}")