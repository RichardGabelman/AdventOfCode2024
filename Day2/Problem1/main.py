lines = open("input.txt", "r").readlines()

numSafe = 0
for line in lines:
    safe = True
    nums = [int(x) for x in line.split()]
    increasing = nums[0] < nums[1]
    for i, n in enumerate(nums):
        if i == 0:
            continue
        if increasing and n < nums[i - 1]:
            safe = False
            break
        if not increasing and n > nums[i - 1]:
            safe = False
            break
        diff = abs(n - nums[i - 1])
        if (diff == 0) or (diff > 3):
            safe = False
            break
    numSafe = numSafe + 1 if safe else numSafe
print(numSafe)