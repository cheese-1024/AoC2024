import re

total = 0
uncorrupted_memory = []
uncorrupted_memory2 = []

with open("input.txt", "r") as f:
  for line in f:
    uncorrupted_memory += re.findall(r'mul\(\d{1,3},\d{1,3}\)', line.strip())

for instruction in uncorrupted_memory:
  total += int(re.findall(r'(?<=mul\()\d{1,3}', instruction)[0]) * int(re.findall(r'mul\(\d{1,3},(\d{1,3})', instruction)[0])

print(total)

with open("input.txt", "r") as f:
  for line in f:
    temp = re.split(r"(mul\(\d{1,3},\d{1,3}\))|(don't\(\))|(do\(\))", line.strip())
    temp2 = [x for x in temp if x is not None]
    temp3 = [x for x in temp2 if re.fullmatch(r'mul\(\d{1,3},\d{1,3}\)', x) is not None or re.fullmatch(r'don\'t\(\)', x) is not None or re.fullmatch(r'do\(\)', x) is not None]
    uncorrupted_memory2 += temp3

total, do = 0, True

for instruction in uncorrupted_memory2:
  if instruction == "don't()":
    do = False
  elif instruction == "do()":
    do = True
  elif do:
    total += int(re.findall(r'(?<=mul\()\d{1,3}', instruction)[0]) * int(re.findall(r'mul\(\d{1,3},(\d{1,3})', instruction)[0])

print(total)