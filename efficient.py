from check import isSorted

# supposed to be a differrent version of the inefficient sorting algo
def effSort(unsortedList):
    lowerList = []
    upperList = []

    lowerList.append(unsortedList[0])
    upperList.append(unsortedList[0])

    unsortedList.pop(0) # pop the first one since its in both lists already

    for num in unsortedList:
        if (num < lowerList[0]):
            lowerList.insert(0, num)

        if (num > upperList[-1]):
            upperList.append(num)

    lowerList.pop() # pop the end of the lower list since it is the first number

    lowerList.extend(upperList)

    return lowerList