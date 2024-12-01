leftList = []
rightList = {}

f = open("input.txt", "r")
lines = f.readlines()

for line in lines:
    left, right = line.split()
    leftList.append(int(left))
    rightList[int(right)] = 1 + rightList.get(int(right), 0)

similarity = 0
for num in leftList:
    similarity += num * rightList.get(num, 0)

print(similarity)