def findSmallest(array):
    smallestIndex = 0
    for i in range(len(array)):
        if array[i] < array[smallestIndex]:
            smallestIndex = i
    return smallestIndex


def selectionSort(array):
    sortedArray = [None] * len(array)
    for i in range(len(array)):
        smallestIndex = findSmallest(array)
        sortedArray[i] = array.pop(smallestIndex)
    return sortedArray


myList = [5, 4, 3, 2, 1]
print(selectionSort(myList))
