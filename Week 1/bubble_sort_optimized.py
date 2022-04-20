array = [1, 23, 21, 231, 22, 211, 12, 22, 22]
length = len(array)
for i in range(length):
    for j in range(length-i-1):
        if(array[j]>array[j+1]):
            array[j], array[j + 1] = array[j + 1], array[j]
print(array)