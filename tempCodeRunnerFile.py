
x = int(input("enter the integer"))
try:
    print("hwllow world"+x)
except (ValueError,TypeError) as e:
    print("something went wrong \n ", e)

        