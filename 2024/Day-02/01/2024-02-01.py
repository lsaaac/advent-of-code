# https://adventofcode.com/2024/day/2 

list_report = []
list_level = []

results_safe = 0

with open("../input.txt") as file:
    for line in file:
        line = line.split()
        line = [int(x) for x in line]  # list comprehension.
        list_report.append(line)

print(list_report)

for level in list_report:
    level_safe = True
    print(level)

    elevation_initial_level = level[1] - level[0]
    elevation_sign = ""

    if elevation_initial_level > 0:
        elevation_sign = "+"
    elif elevation_initial_level < 0:
        elevation_sign = "-"
    else:
        elevation_sign = "0"

    for value in range(0, len(level) - 1):
        elevation_adjacent_levels = level[value + 1] - level[value]
        
        if elevation_adjacent_levels > 0:
            if elevation_sign == "+":
                print("+")
                continue
            else:
                level_safe = False
                print("PROBLEM SLOPE: -+")
        elif elevation_adjacent_levels < 0:
            if elevation_sign == "-":
                print("-")
                continue
            else:
                level_safe = False
                print("PROBLEM SLOPE: +-")
        else:
            level_safe = False
            print("PROBLEM SLOPE: ??")
 

    for value in range(0, len(level) - 1):
        difference_adjacent_levels = abs(level[value + 1] - level[value])

        if difference_adjacent_levels > 3 or difference_adjacent_levels < 1:
            print(f"PROBLEM DIFFERENCE: {difference_adjacent_levels}")
            level_safe = False
        else:
            print(difference_adjacent_levels)
            continue


    if level_safe == True:
        results_safe += 1


print("")
print("RESULTS")
print(results_safe)

