# Lists in PYthon

friends = ["Rakia","Hashim","Junaid","Najma"]
print(friends[0])
print(friends[-1])
print(friends[0][3])
print(friends[1:])
print(friends[1:3])
print(type(friends))
print(len(friends))

countries = list(("Nigeria",2,"america"))
print(countries)

#List method 
list1 = [1,2,3,4,5]
list2 = ["banana","apples","mango","oranges"]
list2.extend(list1)
print(list2)

list2.append("grapers")
print(list2)

list2.insert(3,"cherry")
print(list2)

list2.remove("apples")
print(list2)

print(list2.index("mango"))
print(list2.count("mango"))

list2.reverse()
print(list2)

list3 = list1.copy()

list3.pop()
print(list3)
list2.pop(2)
print(list2)
print(list3)
list2.clear()
print(list2)

del list1
del list2
del list3
# the difference between clear function and del is that clear just remove the content but the del will remove the full variable. means no existance