a = int(input("Enter the first number of the series: "))
b = int(input("Enter the second number of the series: "))
n = int(input("Enter the number of terms needed: "))

print(a, b, end=" ")

count = 2

while count < n:
    c = a + b
    print(c, end=" ")
    a = b
    b = c
    count += 1
