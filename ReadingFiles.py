read_file=open('D:/code/python/Learning/test.txt',"r")
read_file.seek(0)   #Reset cursor to start
print(read_file.readable())
print(read_file.read())   # will read the whole line
print(read_file.readline())  # will read only first line
print(read_file.readlines()[2])   # will read all files and if mentioned then only specific one
for lines in read_file:
  print(lines)

read_file.close()