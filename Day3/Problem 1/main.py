import re

def mul(x, y):
  return x * y

f = open("input.txt", "r").read()

sum = 0

valid_muls = re.findall(r"mul\([0-9]{1,3},[0-9]{1,3}\)", f)
for item in valid_muls:
  values = re.findall("[0-9]+", item)
  x = int(values[0])
  y = int(values[1])
  sum += mul(x, y)

print(sum)