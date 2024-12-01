leftList = []
rightList = []

f = open("input.txt", "r")
lines = f.readlines()

for line in lines:
    left, right = line.split()
    leftList.append(int(left))
    rightList.append(int(right))

leftList.sort()
rightList.sort()
difference = 0
for i in range(len(leftList)):
    difference += abs(rightList[i] - leftList[i])

print(difference)