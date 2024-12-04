wordsearch = []
found = 0

with open("input.txt", "r") as f:
  for line in f:
    wordsearch.append([c for c in line.strip()])

for y in range(len(wordsearch)):
  for x in range(len(wordsearch[y])):
    if wordsearch[y][x] == "X":
      if y < 3:
        if x < 3:
          if wordsearch[y][x+1] == "M":
            if wordsearch[y][x+2] == "A":
              if wordsearch[y][x+3] == "S": 
                found += 1
          if wordsearch[y+1][x+1] == "M":
            if wordsearch[y+2][x+2] == "A":
              if wordsearch[y+3][x+3] == "S":
                found += 1
          if wordsearch[y+1][x] == "M":
            if wordsearch[y+2][x] == "A":
              if wordsearch[y+3][x] == "S":
                found += 1
        elif x >= 3 and x < len(wordsearch[y])-3:
          if wordsearch[y][x-1] == "M":
            if wordsearch[y][x-2] == "A":
              if wordsearch[y][x-3] == "S":
                found += 1
          if wordsearch[y+1][x-1] == "M":
            if wordsearch[y+2][x-2] == "A":
              if wordsearch[y+3][x-3] == "S":
                found += 1
          if wordsearch[y][x+1] == "M":
            if wordsearch[y][x+2] == "A":
              if wordsearch[y][x+3] == "S": 
                found += 1
          if wordsearch[y+1][x+1] == "M":
            if wordsearch[y+2][x+2] == "A":
              if wordsearch[y+3][x+3] == "S":
                found += 1
          if wordsearch[y+1][x] == "M":
            if wordsearch[y+2][x] == "A":
              if wordsearch[y+3][x] == "S":
                found += 1
        else: 
          if wordsearch[y+1][x] == "M":
            if wordsearch[y+2][x] == "A":
              if wordsearch[y+3][x] == "S":
                found += 1
          if wordsearch[y+1][x-1] == "M":
            if wordsearch[y+2][x-2] == "A":
              if wordsearch[y+3][x-3] == "S":
                found += 1
          if wordsearch[y][x-1] == "M":
            if wordsearch[y][x-2] == "A":
              if wordsearch[y][x-3] == "S":
                found += 1
      elif y >= 3 and y < len(wordsearch)-3:    
        if x < 3:
          if wordsearch[y-1][x] == "M":
            if wordsearch[y-2][x] == "A":
              if wordsearch[y-3][x] == "S":
                found += 1
          if wordsearch[y-1][x+1] == "M":
            if wordsearch[y-2][x+2] == "A":
              if wordsearch[y-3][x+3] == "S":
                found += 1
          if wordsearch[y][x+1] == "M":
            if wordsearch[y][x+2] == "A":
              if wordsearch[y][x+3] == "S": 
                found += 1
          if wordsearch[y+1][x+1] == "M":
            if wordsearch[y+2][x+2] == "A":
              if wordsearch[y+3][x+3] == "S":
                found += 1
          if wordsearch[y+1][x] == "M":
            if wordsearch[y+2][x] == "A":
              if wordsearch[y+3][x] == "S":
                found += 1
        elif x >= 3 and x < len(wordsearch[y])-3:
          if wordsearch[y-1][x] == "M":
            if wordsearch[y-2][x] == "A":
              if wordsearch[y-3][x] == "S":
                found += 1
          if wordsearch[y][x-1] == "M":
            if wordsearch[y][x-2] == "A":
              if wordsearch[y][x-3] == "S":
                found += 1
          if wordsearch[y][x+1] == "M":
            if wordsearch[y][x+2] == "A":
              if wordsearch[y][x+3] == "S": 
                found += 1
          if wordsearch[y+1][x+1] == "M":
            if wordsearch[y+2][x+2] == "A":
              if wordsearch[y+3][x+3] == "S":
                found += 1
          if wordsearch[y+1][x] == "M":
            if wordsearch[y+2][x] == "A":
              if wordsearch[y+3][x] == "S":
                found += 1
          if wordsearch[y+1][x-1] == "M":
            if wordsearch[y+2][x-2] == "A":
              if wordsearch[y+3][x-3] == "S":
                found += 1
          if wordsearch[y-1][x+1] == "M":
            if wordsearch[y-2][x+2] == "A":
              if wordsearch[y-3][x+3] == "S":
                found += 1
          if wordsearch[y-1][x-1] == "M":
            if wordsearch[y-2][x-2] == "A":
              if wordsearch[y-3][x-3] == "S":
                found += 1
        else:
          if wordsearch[y-1][x] == "M":
            if wordsearch[y-2][x] == "A":
              if wordsearch[y-3][x] == "S":
                found += 1
          if wordsearch[y-1][x-1] == "M":
            if wordsearch[y-2][x-2] == "A":
              if wordsearch[y-3][x-3] == "S":
                found += 1
          if wordsearch[y][x-1] == "M":
            if wordsearch[y][x-2] == "A":
              if wordsearch[y][x-3] == "S":
                found += 1
          if wordsearch[y+1][x-1] == "M":
            if wordsearch[y+2][x-2] == "A":
              if wordsearch[y+3][x-3] == "S":
                found += 1
          if wordsearch[y+1][x] == "M":
            if wordsearch[y+2][x] == "A":
              if wordsearch[y+3][x] == "S":
                found += 1
      else:
        if x < 3:
          if wordsearch[y-1][x] == "M":
            if wordsearch[y-2][x] == "A":
              if wordsearch[y-3][x] == "S":
                found += 1
          if wordsearch[y-1][x+1] == "M":
            if wordsearch[y-2][x+2] == "A":
              if wordsearch[y-3][x+3] == "S":
                found += 1
          if wordsearch[y][x+1] == "M":
            if wordsearch[y][x+2] == "A":
              if wordsearch[y][x+3] == "S": 
                found += 1
        elif x >= 3 and x < len(wordsearch[y])-3:
          if wordsearch[y][x-1] == "M":
            if wordsearch[y][x-2] == "A":
              if wordsearch[y][x-3] == "S":
                found += 1
          if wordsearch[y-1][x-1] == "M":
            if wordsearch[y-2][x-2] == "A":
              if wordsearch[y-3][x-3] == "S":
                found += 1
          if wordsearch[y-1][x] == "M":
            if wordsearch[y-2][x] == "A":
              if wordsearch[y-3][x] == "S":
                found += 1
          if wordsearch[y-1][x+1] == "M":
            if wordsearch[y-2][x+2] == "A":
              if wordsearch[y-3][x+3] == "S":
                found += 1
          if wordsearch[y][x+1] == "M":
            if wordsearch[y][x+2] == "A":
              if wordsearch[y][x+3] == "S": 
                found += 1
        else:
          if wordsearch[y-1][x] == "M":
            if wordsearch[y-2][x] == "A":
              if wordsearch[y-3][x] == "S":
                found += 1
          if wordsearch[y-1][x-1] == "M":
            if wordsearch[y-2][x-2] == "A":
              if wordsearch[y-3][x-3] == "S":
                found += 1
          if wordsearch[y][x-1] == "M":
            if wordsearch[y][x-2] == "A":
              if wordsearch[y][x-3] == "S":
                found += 1

print("part1: " + str(found))
found = 0 

for y in range(1, len(wordsearch)-1):
  for x in range(1, len(wordsearch[y])-1):
    if wordsearch[y][x] == "A":
      if wordsearch[y-1][x-1] == "M":
        if wordsearch[y-1][x+1] == "S":
          if wordsearch[y+1][x-1] == "M":
            if wordsearch[y+1][x+1] == "S":
              found += 1
      if wordsearch[y-1][x-1] == "M":
        if wordsearch[y-1][x+1] == "M":
          if wordsearch[y+1][x-1] == "S":
            if wordsearch[y+1][x+1] == "S":
              found += 1
      if wordsearch[y-1][x-1] == "S":
        if wordsearch[y-1][x+1] == "M":
          if wordsearch[y+1][x-1] == "S":
            if wordsearch[y+1][x+1] == "M":
              found += 1
      if wordsearch[y-1][x-1] == "S":
        if wordsearch[y-1][x+1] == "S":
          if wordsearch[y+1][x-1] == "M":
            if wordsearch[y+1][x+1] == "M":
              found += 1

print("part2: " + str(found))
      


      