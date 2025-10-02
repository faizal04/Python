matrix = [
    [1,2,3],
    [4,5,6],
    [7,8,9]
]
print(matrix)

print(matrix[0])


print(matrix[0][1])


# transform the above matrix
transpose=[]
# data flow 
# get length of 1 row
# get length of total list
# append in transpose matrix only ist coloum that is 00 10 20 keep increasing the value of row and let the column remain same 
# .....


for i in range(len(matrix[0])):
    row=[]
    for j in range(len(matrix)):
        row.append(matrix[j][i])
    transpose.append(row)

for x in transpose:
    print(x)

