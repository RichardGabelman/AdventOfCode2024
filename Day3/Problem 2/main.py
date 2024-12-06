import re

def mul(x, y):
  return x * y

f = open("input.txt", "r").read()

sum = 0

# every valid multiple
valid_muls = re.findall(r"mul\([0-9]{1,3},[0-9]{1,3}\)", f)
# split the file up into the strings between each valid multiple
split_up = re.split(r"mul\([0-9]{1,3},[0-9]{1,3}\)", f)
last_conditional = True
for i, exp in enumerate(valid_muls):
  # look for a do or a don't in the immediate preceding string
  dos_and_donts = re.findall(r"do\(\)|don't\(\)", split_up[i])
  if len(dos_and_donts) > 0 and dos_and_donts[-1] == "don't()":
    last_conditional = False
    continue
  if len(dos_and_donts) > 0:
    last_conditional = True
  else:
    # no immediately preceding do/dont, defer to most recent
    if not last_conditional:
      continue
  values = re.findall("[0-9]+", exp)
  x = int(values[0])
  y = int(values[1])
  sum += mul(x, y)

print(sum)