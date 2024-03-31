def isSorted(sortedList):
    for num in range(len(sortedList)):
        if num + 1 < len(sortedList):
            if (sortedList[num] > sortedList[num + 1]):
                return False
            
    return True