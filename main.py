from check import isSorted
from inefficient import ineffSort
from efficient import effSort
from random import randint
import time

def getRandomList():
    randList = []

    for _ in range(randint(1000, 10000)):
        randList.append(randint(0, 1000))

    return randList

def testIneffSort():
    randList = getRandomList()

    sortedList = ineffSort(randList)

    if (isSorted(sortedList) == False):
        print(f"Length : {len(sortedList)} List is not sorted: {sortedList}")

def testEffSort():
    randList = getRandomList()

    sortedList = effSort(randList)

    if (isSorted(sortedList) == False):
        print(f"Length : {len(sortedList)} List is not sorted: {sortedList}")

def testNormal():
    randList = getRandomList()

    randList.sort()

    if (isSorted(randList) == False): # keeping this so it also has to go through the checks of this in order to keep consistency
        print(f"Length : {len(randList)} List is not sorted: {randList}")

testingNumbers = 100000

print(f"Each algorithm will be tested {testingNumbers} times.")

# super slow so this one isnt shown, but i keep the code bc it was what i used to make the more efficient algorithm
# print("Testing inefficient sorting...")

# ineffStartTime = time.time()

# for _ in range(testingNumbers): # testing the inefficient sorting algo
#     testIneffSort()

# ineffEndTime = time.time()

# print(f"Ineff done - elapsed time: {ineffEndTime - ineffStartTime}")

effStartTime = time.time()

print("Testing efficient sorting...")
for _ in range(testingNumbers):
    testEffSort()

effEndTime = time.time()

print(f"Eff done - elapsed time: {effEndTime - effStartTime}")

normStartTime = time.time()

print("Testing normal sorting...")
for _ in range(testingNumbers):
    testNormal() # the normal python sorting algorithm, which might be slower than mine

normEndTime = time.time()

print(f"Normal done - elapsed time: {normEndTime - normStartTime}")