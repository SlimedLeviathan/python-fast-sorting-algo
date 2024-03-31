import math
from check import isSorted

# a sorting algorithm where we find the min and max and set them to the start and end of the list
def ineffSort(unsortedList):
    index = 0
    middle = math.floor(len(unsortedList) / 2)

    while True:

        if (index > middle or isSorted(unsortedList)): # once it gets to the middle of the list or is sorted
            break

        # finds the index of the min and the max
        minIndex = index
        maxIndex = index

        for num in range(len(unsortedList) - (index * 2)):

            num = num + index

            if (unsortedList[num] < unsortedList[minIndex]):
                minIndex = num

            if (unsortedList[num] > unsortedList[maxIndex]):
                maxIndex = num

        # take the min and max out and then set them to the start and end of the list
        if (minIndex < maxIndex):
            minValue = unsortedList.pop(minIndex)

            unsortedList.insert(index, minValue)
            
            maxValue = unsortedList.pop(maxIndex)

            unsortedList.insert(len(unsortedList) - index, maxValue)
        
        else:
            maxValue = unsortedList.pop(maxIndex)

            unsortedList.insert(len(unsortedList) - index, maxValue)
            
            minValue = unsortedList.pop(minIndex - 1)

            unsortedList.insert(index, minValue)

        index += 1

    return unsortedList