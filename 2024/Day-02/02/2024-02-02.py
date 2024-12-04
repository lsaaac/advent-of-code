# https://adventofcode.com/2024/day/2 

list_report = []
list_level = []

level_safe = True
results_safe = 0

with open("../input.txt") as file:
    for line in file:
        line = line.split()
        line = [int(x) for x in line]  # list comprehension.
        list_report.append(line)

#print(list_report)

def adjacent_elements_difference(level):
# Take a list of numbers and tests them to see if they adjacantly have a
# difference between 1 - 3. If they do, return nothing, if they don't return the
# positions of the two offending values.  

#    print(level)
    for value in range(0, len(level) - 1):
        difference_adjacent_levels = abs(level[value + 1] - level[value])

        if difference_adjacent_levels > 3 or difference_adjacent_levels < 1:
#            print(f"DIFF ERROR POSITION: {value}")
#            print(f"{value}, {value + 1}")
#            list_value_errors = [value, (value + 1)]
#            return list_value_errors
            return [value, (value + 1)] 
        else:
            continue

def adjacent_elements_slope(level):
# Slope is either: Positive (> 0)
#                  Negative (< 0)
#                  Zero

#    print(level)
    slope_level_initial = level[1] - level[0] 
    for value in range(1, len(level) -1):
        slope_level_current = level[value + 1] - level[value]

        #print(f"POS.{value}: {slope_level_initial}, {slope_level_current}")

        if slope_level_initial > 0 and slope_level_current > 0:  # Both Positive
            slope_level_initial = slope_level_current 
        elif slope_level_initial < 0 and slope_level_current < 0:  # Both Negative             
            slope_level_initial = slope_level_current
        else:  # Zero or conflicting
            #print(f"SLOPE ERROR POSITION: {value}")
            #print(f"{value}, {value + 1}")
            return [value, value + 1]            


#print("LIST TEST: DIFFERENCE")

#for level in list_report:
#    print(level)
#    print(adjacent_elements_difference(level))
#    if adjacent_elements_difference(level):
#        print(adjacent_elements_difference(level))
#        print(type(adjacent_elements_difference(level)))
#    else:
#        continue

#print("LIST TEST: SLOPE")

#for level in list_report:
#    adjacent_elements_slope(level)


for level in list_report:
    level_safe = True
    set_report_errors = set() 

#    print(level)

#    set_report_errors.update(adjacent_elements_difference(level)) 

    if adjacent_elements_difference(level):
#        print("DIFF ERROR ON CURRENT LEVEL")
        set_report_errors.update(adjacent_elements_difference(level))
        level_safe = False
#        print(f"ERRORS: {set_report_errors}")
#        print(set_report_errors)
    else:
#        print("DIFF TEST COMPLETE GOOD")
        pass 

    if adjacent_elements_slope(level):
#        print("SLOPE ERROR ON CURRENT LEVEL")
        set_report_errors.update(adjacent_elements_slope(level))
        level_safe = False
#        print(f"ERRORS: {set_report_errors}")
#        print(set_report_errors)
    else:
#        print("SLOPE TEST COMPLETE GOOD")
        pass 
   
#    print(set_report_errors)

    if set_report_errors:
#        print("FURTHER TESTING REQUIRED")
        print("RECHECK BAD LEVEL")
        print(level)
        for value in set_report_errors:
            level_safe = True
            list_recheck = level.copy()
            del(list_recheck[value])
            print(list_recheck)
            
            if adjacent_elements_difference(list_recheck):
                print("DIFF ERROR ON CURRENT LEVEL")
                #set_report_errors.update(adjacent_elements_difference(level))
                level_safe = False
#                print(f"ERRORS: {set_report_errors}")
            else:
                print("DIFF TEST COMPLETE GOOD")
                pass

            if adjacent_elements_slope(list_recheck):
#                print(adjacent_elements_slope(level))
                print("SLOPE ERROR ON CURRENT LEVEL")
   #            set_report_errors.update(adjacent_elements_slope(level))
                level_safe = False
#                print(f"ERRORS: {set_report_errors}")
            else:
                print("SLOPE TEST COMPLETE GOOD")
                pass
        
            if level_safe == True:
                print("***LEVEL GOOD***")
                break 
            else:
                print("***LEVEL BAD***")
            
    else:
#        print("LEVEL GOOD")
        pass

#    f = open("output.txt", "a")

    if level_safe == True:
#        print(f"LEVEL GOOD: {level}", file=f)
        results_safe += 1 
    else:
#        print(f"LEVEL BAD:  {level} {set_report_errors}", file=f)
        continue

#    f.close()


print(f"SAFE LEVELS: {results_safe}")
#    print(level_safe)
            
#    if adjacent_elements_slope(level):
#        set_report_errors.update(adjacent_elements_slope(level))
#        level_safe = False
#    else:
#        continue
#

#list_test_good = [7,6,4,2,1]
#list_test_bad = [8,6,7,4,1]
#adjacent_elements_safe(list_test_good)
#list_test_output = adjacent_elements_safe(list_test_bad)
#adjacent_elements_slope(list_test_bad)
#print(list_test_output)
#for level in list_report:
#    level_safe = True
#    print(level)
#
#    elevation_initial_level = level[1] - level[0]
#    elevation_sign = ""
#
#    if elevation_initial_level > 0:
#        elevation_sign = "+"
#    elif elevation_initial_level < 0:
#        elevation_sign = "-"
#    else:
#        elevation_sign = "0"
#
#    for value in range(0, len(level) - 1):
#        elevation_adjacent_levels = level[value + 1] - level[value]
#        
#        if elevation_adjacent_levels > 0:
#            if elevation_sign == "+":
#                print("+")
#                continue
#            else:
#                level_safe = False
#                print("PROBLEM SLOPE: -+")
#        elif elevation_adjacent_levels < 0:
#            if elevation_sign == "-":
#                print("-")
#                continue
#            else:
#                level_safe = False
#                print("PROBLEM SLOPE: +-")
#        else:
#            level_safe = False
#            print("PROBLEM SLOPE: ??")
# 
#
#    for value in range(0, len(level) - 1):
#        difference_adjacent_levels = abs(level[value + 1] - level[value])
#
#        if difference_adjacent_levels > 3 or difference_adjacent_levels < 1:
#            print(f"PROBLEM DIFFERENCE: {difference_adjacent_levels}")
#            level_safe = False
#        else:
#            print(difference_adjacent_levels)
#            continue
#
#
#    if level_safe == True:
#        results_safe += 1
#
#
#print("")
#print("RESULTS")
#print(results_safe)
