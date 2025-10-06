read_file=open("test.txt","r")
print(read_file.readable())
print(read_file.read())   # will read the whole line
print(read_file.readline())  # will read only first line
print(read_file.readlines()[1])   # will read all files and if mentioned then only specific one

read_file.close()