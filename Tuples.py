#tuples 

#same as list but the only difference is that tuples are immutable they can't change 

tuple1 =(1,2,3,4,5)
# tuple1[2] =0    # error
print(tuple1)
tuple2 =("faisal","harray","hashim","junaid")
# tuple1.extend(tuple2)   # can't because as we already know tuple are immutable means neither we can add nor insert nothing
print(tuple1)

tuple_3 = tuple(("hellow","world"))
print(tuple_3)