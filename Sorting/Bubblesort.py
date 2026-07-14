arr = [64, 29, 12, 2, 11]
while True:
    swapped = False
    for i in range(len(arr) - 1):
            
            if arr[i] > arr[i + 1]: 

                temp = arr[i]
                arr[i] = arr[i+1]
                arr[i+1] = temp

                swapped = True
    print(arr)

    if not swapped:
        break    



