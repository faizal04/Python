try:
    x = int(input("Enter the integer"))
    print(x)
except Exception as e:
    print("something went wrong in the try block \n the error is ", e)
else:
    print("Nothing went wrong")
finally:
    print("Code excecution ends")


# raise error 
x = input("Enter the integer")
if type(x) == str:
    raise ValueError("you entered string rather than integer")

# grabing multiple exceptions

x = int(input("enter the integer"))
try:
    print("hwllow world"+x)
except (ValueError,TypeError) as e:
    print("something went wrong \n ", e)

        