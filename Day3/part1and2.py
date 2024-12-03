import re

uncorrupted_memory, sol1, sol2, do = [], 0, 0, True

with open("input.txt", "r") as f:
  for line in f:
    split = re.split(r"(mul\(\d{1,3},\d{1,3}\))|(don't\(\))|(do\(\))", line.strip()) 
    removeNone = [x for x in split if x is not None]
    removeCorrupted = [x for x in removeNone if re.fullmatch(r'mul\(\d{1,3},\d{1,3}\)', x) is not None or re.fullmatch(r'don\'t\(\)', x) is not None or re.fullmatch(r'do\(\)', x) is not None]
    uncorrupted_memory += removeCorrupted

for instruction in uncorrupted_memory:
  if instruction != "do()" and instruction != "don't()":
    sol1 += int(re.findall(r'(?<=mul\()\d{1,3}', instruction)[0]) * int(re.findall(r'mul\(\d{1,3},(\d{1,3})', instruction)[0])
  if instruction == "don't()":
    do = False
  elif instruction == "do()":
    do = True
  elif do:
    sol2 += int(re.findall(r'(?<=mul\()\d{1,3}', instruction)[0]) * int(re.findall(r'mul\(\d{1,3},(\d{1,3})', instruction)[0])

print(sol1, sol2)