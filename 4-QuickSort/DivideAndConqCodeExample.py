def mySum(arr):
    total = 0
    for element in arr:
        total += element
    return total


def mySumDAndC(arr):
    if not arr:
        return 0
    return arr[0] + mySumDAndC(arr[1:len(arr)])


myNums = [3, 2, 5, 99, 0, 100]
print(mySum(myNums))
print(mySumDAndC(myNums))
