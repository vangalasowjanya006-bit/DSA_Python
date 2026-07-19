def bubble_sort(arr, n):

    if n == 1:
        return

    for i in range(n - 1):

        if arr[i] > arr[i + 1]:

            temp = arr[i]
            arr[i] = arr[i + 1]
            arr[i + 1] = temp

    print(arr)
    bubble_sort(arr, n - 1)

arr = [64, 29, 12, 2, 11]
bubble_sort(arr, len(arr))
print("\nSorted Array:", arr)
