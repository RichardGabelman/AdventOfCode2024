def xmas_count(file):
  f = open(file, 'r')
  
  lines = f.readlines()

  xmas_count = 0

  for i in range(len(lines)):
    #left and right case
    xmas_count += lines[i].count('XMAS')
    xmas_count += lines[i].count('SAMX')

    for j in range(len(lines[i])):

      if lines[i][j] == 'X':
        #down case
        if (i + 3) <= (len(lines) - 1):
          if lines[i+1][j] == 'M' and lines[i+2][j] == 'A' and lines[i+3][j] == 'S':
            xmas_count += 1
        #up case
        if (i - 3) >= 0:
          if lines[i-1][j] == 'M' and lines[i-2][j] == 'A' and lines[i-3][j] == 'S':
            xmas_count += 1
        #down right case
        if (i + 3) <= (len(lines) - 1) and (j + 3) <= (len(lines[i]) - 1):
          if lines[i+1][j+1] == 'M' and lines[i+2][j+2] == 'A' and lines[i+3][j+3] == 'S':
            xmas_count += 1
        #down left case
        if (i + 3) <= (len(lines) - 1) and (j - 3) >= 0:
          if lines[i+1][j-1] == 'M' and lines[i+2][j-2] == 'A' and lines[i+3][j-3] == 'S':
            xmas_count += 1
        #up left case
        if (i - 3) >= 0 and (j - 3) >= 0:
          if lines[i-1][j-1] == 'M' and lines[i-2][j-2] == 'A' and lines[i-3][j-3] == 'S':
            xmas_count += 1
        #up right case
        if (i - 3) >= 0 and (j + 3) <= (len(lines[i]) - 1):
          if lines[i-1][j+1] == 'M' and lines[i-2][j+2] == 'A' and lines[i-3][j+3] == 'S':
            xmas_count += 1

  return xmas_count

print(xmas_count('input.txt'))