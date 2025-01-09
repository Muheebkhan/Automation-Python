import array

arr = array.array('i', [10, 20, 30, 40, 50])
print(arr)
print(arr[0])
print(arr[1:4])

arr.append(60)
print(arr)
arr.remove(30)
print(arr)

for element in arr:
    print(element)

    print((arr.index(50)))