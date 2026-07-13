arr = [64, 25, 12, 22, 11]

for i in range(len(arr) - 1):
    smallest = i

    for j in range(i + 1, len(arr)):
        if arr[smallest] > arr[j]:
            smallest = j

    temp = arr[i]
    arr[i] = arr[smallest]
    arr[smallest] = temp

print(arr)