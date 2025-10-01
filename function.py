def print_function():
    print("this function is just for learning the syntax of the function")

print_function()

def argument_function(*name):  #The * operator in parameters packs multiple values into a tuple.
    print(name)

argument_function("faisal","john")

def dictonary_function(**info):
     #** in a function parameter, Python takes all the extra keyword arguments (the ones written like key=value)   and packs them into a dictionary, where:
# Key → the argument name

# Value → the value you passed
    print("the available detail is ",info)

dictonary_function(name="faisal",age=20,university="IUST")