age1 = int(input("enter your Age"))
age2 =int(input("Enter your friend age"))

if age1>age2 or age2<age1:
    print("you are older than your friend",age2-age1)
else:
    print("your friend is older than you by",age2-age1,"years")