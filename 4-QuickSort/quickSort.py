import random


def quickSort(arr):
    if len(arr) >= 2:
        pivotIndex = random.randint(0, len(arr) - 1)
        pivot = arr[pivotIndex]
        slicedArr = arr[0:pivotIndex] + arr[pivotIndex + 1:]
        lessThanSubArray = [i for i in slicedArr if i <= pivot]
        greaterThanSubArray = [i for i in slicedArr if i > pivot]
        arr = quickSort(lessThanSubArray) + [pivot] + quickSort(greaterThanSubArray)
    return arr


myNums = [3, 2, 5, 99, 0, 100]
print(quickSort(myNums))
