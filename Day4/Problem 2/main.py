def x_mas_count(file):
  f = open(file, 'r')
  
  lines = f.readlines()

  x_mas_count = 0

  for i in range(len(lines)):

    for j in range(len(lines[i])):

      if lines[i][j] == 'A':
        #tl->br diagonal
        if (i - 1) >= 0 and (i + 1) <= (len(lines) - 1) and (j - 1) >= 0 and (j + 1) <= (len(lines[i]) - 1):
          if ((lines[i-1][j-1] == 'M') and (lines[i+1][j+1] == 'S')) or ((lines[i-1][j-1] == 'S') and (lines[i+1][j+1] == 'M')):
            if ((lines[i-1][j+1] == 'M') and (lines[i+1][j-1] == 'S')) or ((lines[i-1][j+1] == 'S') and (lines[i+1][j-1] == 'M')):
              x_mas_count += 1

  return x_mas_count

print(x_mas_count('input.txt'))