safe = 0
reportList = []

with open("""E:\Tommy\Documents\Coding\AoC2024\Day2\input.txt""", "r") as reports:
    for line in reports:
        reportList.append(line.split())

reportList = [[int(num) for num in line] for line in reportList]

for report in reportList:
    if (all(report[i] <= report[i + 1] for i in range(len(report) - 1))) or (all(report[i] >= report[i + 1] for i in range(len(report) - 1))):
        difference = 0
        for i in range(len(report)-1):
            if abs(report[i] - report[i+1]) > difference:
                difference = abs(report[i] - report[i+1])
            elif abs(report[i] - report[i+1]) == 0:
                difference = 0
                break
        if difference >= 1 and difference <= 3:
            safe += 1

print(safe)
safe = 0              

for report in reportList:
    madesafe = False
    if madesafe == False:
        for idx, num in enumerate(report):
            temp = report.pop(idx)
            if (all(report[i] <= report[i + 1] for i in range(len(report) - 1))) or (all(report[i] >= report[i + 1] for i in range(len(report) - 1))):
                difference = 0
                for i in range(len(report)-1):
                    if abs(report[i] - report[i+1]) > difference:
                        difference = abs(report[i] - report[i+1])
                    elif abs(report[i] - report[i+1]) == 0:
                        difference = 0
                        break
                if difference >= 1 and difference <= 3:
                    safe += 1
                    madesafe = True   
            report.insert(idx, temp)
            if madesafe == True:
                break

print(str(safe))