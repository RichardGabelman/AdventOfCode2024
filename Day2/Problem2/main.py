lines = open("input.txt", "r").readlines()


def allDecreasing(arr):
    for i, n in enumerate(arr):
      if i == 0:
          continue
      if n >= arr[i - 1]:
          return False
    return True
def mostDecreasing(arr):
    if allDecreasing(arr):
        return [idx for idx in range(len(arr))]
    potentialRemoved = []
    for i in range(len(arr)):
        copy = arr.copy()
        del copy[i]
        if allDecreasing(copy):
            potentialRemoved.append(i)
    return potentialRemoved

def allIncreasing(arr):
    for i, n in enumerate(arr):
      if i == 0:
          continue
      if n <= arr[i - 1]:
          return False
    return True
def mostIncreasing(arr):
    if allIncreasing(arr):
        return [idx for idx in range(len(arr))]
    potentialRemoved = []
    for i in range(len(arr)):
        copy = arr.copy()
        del copy[i]
        if allIncreasing(copy):
          potentialRemoved.append(i)
    return potentialRemoved

def allDifference(arr, threshold):
    for i, n in enumerate(arr):
        if i == 0:
            continue
        if abs(n - arr[i - 1]) > threshold:
            return False
    return True
def mostDifference(arr, threshold):
    if allDifference(arr, threshold):
        return [idx for idx in range(len(arr))]
    potentialRemoved = []
    for i in range(len(arr)):
        copy = arr.copy()
        del copy[i]
        if allDifference(copy, threshold):
          potentialRemoved.append(i)
    return potentialRemoved


def shareAtLeastOne(arr1, arr2):
    for i in arr1:
        if i in arr2:
            return True
    return False


numSafe = 0
for line in lines:
    safe = True
    nums = [int(x) for x in line.split()]
    if shareAtLeastOne(mostDecreasing(nums), mostDifference(nums, 3)) or shareAtLeastOne(mostIncreasing(nums), mostDifference(nums, 3)):
        numSafe += 1
print(numSafe)