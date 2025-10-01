if 5>6:
    print("5 is greater than 6")
elif 7<9:
    print("7 is less than 9")
else:
    print("none of the above condition work")


#example
# age checker by taking the input from the user

age1 = int(input("enter your Age"))
age2 =int(input("Enter your friend age"))

if age1>age2 or age2<age1:
    print("you are older than your friend",age2-age1)
else:
    print("your friend is older than you by",age2-age1,"years")