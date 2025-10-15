arr = [25, 2, 55, 45, 92, 38, 87, 90, 66, 56, 97]
print("Original list: ", arr)
l, r = 0, len(arr)-1
while l < r:
    arr[l], arr[r] = arr[r], arr[l]
    l +=1
    r -=1
print("Reversed List: ", arr)