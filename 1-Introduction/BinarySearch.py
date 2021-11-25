def binarySearch(arrayToSearch, target):
    low = 0
    high = len(arrayToSearch) - 1
    while low <= high:
        mid = (low + high) // 2
        if arrayToSearch[mid] == target:
            return mid
        elif arrayToSearch[mid] > target:
            high = mid - 1
        else:
            low = mid + 1
    return -1


myList = [1, 3, 5, 7, 9]
print(binarySearch(myList, 2))
print(binarySearch(myList, 3))
print(binarySearch(myList, 4))
print(binarySearch(myList, 6))
print(binarySearch(myList, 7))
