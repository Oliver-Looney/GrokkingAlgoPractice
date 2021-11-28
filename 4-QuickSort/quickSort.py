def quickSort(arr):
    if len(arr) >= 2:
        pivot = arr[0]
        lessThanSubArray = [i for i in arr[1:] if i <= pivot]
        greaterThanSubArray = [i for i in arr[1:] if i > pivot]
        arr = quickSort(lessThanSubArray) + [pivot] + quickSort(greaterThanSubArray)
    return arr


myNums = [3, 2, 5, 99, 0, 100]
print(quickSort(myNums))
