list1 = [1, 5, 87, 'Aidah', 'This is a list']
print(list1)
print(list1[0]) #print ist element
print(list1[-1]) #print last element
print(len(list1)) #print length of list
list1.append('append') # add at end
print(list1)
list1.extend((2,0)) #single elements added
print(list1)
list1.insert(3, 22) # adds at implied index
print(list1)
list1.remove('Aidah') # removes the implied entry - the value not value at index
print(list1)
a = list1.pop(2) #removes by index
print(a)
del list1[0] #removes the entry at implied index
print(list1)
list1[0] = 14 #updates element at implied index by given value
print(list1)
print(list1[1:3])# slices list includes 1 index, excludes 3 index
#list1.sort #should only be numbers to work => ascending order
#print(list1)
#list1.sort(reverse=True) =>descending order
list1.reverse()
print(list1)
print(2 in list1) #checking element exisitance
print(list1.index('append')) #finding index
print(list1.count(22)) #counting occurances
new_list = list1.copy()
print("this is the copied list: ", new_list)
new_list.clear()
print(new_list)
