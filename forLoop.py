for letter in "Hello":
    print(letter)


# enumerate is a built-in Python function that adds a counter (index) to any iterable while looping over it.

names = list(("jiraya","bankai","pain","naruto","sasuke","tanjiro"))

for i,n in enumerate(names):
    print(i,n)



my_info ={
    "name":"faisal",
    "age":21,
    "stream":"CSE",
    "Semester":5,
    "university":"Islamic University of Science and Technology"
}


for key, values in my_info.items():
    print(key,values)
    if values == "CSE":
        break

for values in my_info:
    print(values)   # it will print only keys

for values in my_info:
    print(my_info[values])  # give only values


for x in range(4,7):
    print(x)

for x in range(10):
    print(x)

# we can also use else statement in for loop 
print("printing the value to 10 and with else Statement")
for x in range(10):
    print(x)
else:
    print("Loop finished")