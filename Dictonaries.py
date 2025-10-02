my_dict ={
    "name":"faisal",
    "age":21,
    "university":"Islamic University of Science and Technology",
    "friends":["suhail","hashim","junaid"]
}

print(my_dict)
print(my_dict["name"])
# print(my_dict.name)   # not possible in python
print(type(my_dict))

my_dict["age"] = 22      # update the data
my_dict["State"] ="Kashmir"   # add new key value in dict 
print(my_dict)


del my_dict
print(my_dict)   # error because my_dict is already deleted

#same as js object but no prototype chain e.g my_dict.toString() is not possible but it is possible in js 
# no dot notation can be used in the python like in js. e.g my_dict.name is not possible in python but is possible in js
