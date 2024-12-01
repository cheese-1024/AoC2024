list1, list2 = [], []
totalDist = 0
similarity = 0

# split file into lists and sort ascending
with open("input.txt", "r") as locList:
  for line in locList:
    list1.append(int(line.strip()[:5]))
    list2.append(int(line.strip()[8:]))
list1.sort()
list2.sort()

# find total distance by adding differences between rows (pt1)
for i in range(len(list1)):
  totalDist += abs(list1[i] - list2[i])
print(totalDist)

# find similarity score, multiply number by amount of occurences in second column (pt2)
for i in range(len(list1)):
  similarity += list1[i] * list2.count(list1[i])
print(similarity)